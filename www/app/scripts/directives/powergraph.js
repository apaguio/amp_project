/* jshint quotmark: false */
/* global d3, _ */
'use strict';

(function() {

    var duration = 4900;
    var marginBetween = 30;
    var parseDate = d3.time.format("%b %Y").parse;
    var bisectDate = d3.bisector(function(d) { return d.time; }).left;

    function plot(scope, el, data, config) {

        if (!data || !data.length) {
            return;
        }

        scope.start = scope.min.time;
        scope.end = scope.max.time;
        scope.margin = {top: 0, right: 20, bottom: 20, left: 40};
        scope.width = el.width();
        scope.height = el.height();
        
        if (scope.zoom) {
            scope.zoomHeight = 100;
            scope.height -= scope.zoomHeight;
        } else {
            scope.zoomHeight = 0;
        }
        scope.bigheight = scope.height / 2;
        if (config.graphs) {
            scope.bigheight = !!config.graphs.consumption ? scope.height / 2 : 0;
        }
        scope.smallheight = ((scope.height - scope.bigheight) / 2);
        if (config.graphs && (!config.graphs.voltage || !config.graphs.powerfactor)) {
            scope.smallheight += scope.smallheight;
        }
        if (config.graphs && (!config.graphs.voltage && !config.graphs.powerfactor)) {
            scope.bigheight += scope.bigheight;
        }

        // Adding General X scale
        scope.x = d3.time.scale().range([0, scope.width - scope.margin.left - scope.margin.right]);
        scope.x.domain([moment(scope.start).toDate(), moment(scope.end).toDate()]);

        if (scope.zoom) {
            // Adding zoom X Scale
            scope.zoomX = d3.time.scale().range([0, scope.width - scope.margin.left - scope.margin.right]);
            scope.zoomX.domain([moment(scope.start).toDate(), moment(scope.end).toDate()]);

            scope.brushed = function () {
                scope.x.domain(scope.brush.empty() ? scope.zoomX.domain() : scope.brush.extent());
                // Updating other graphs
                update(scope, data, config);
            };
            scope.brush = d3.svg.brush()
                .x(scope.zoomX)
                .on("brush", scope.brushed);
        }

        scope.y = d3.scale.linear().range([scope.bigheight - marginBetween, 0]);
        var minY = _.min([scope.min.net, 0]);
        console.log("MIN Y : ", minY);
        var maxY = _.max([scope.max.P]);
        scope.y.domain([minY, Math.max(config.maxDemand, maxY)]);
        scope.y.axis = d3.svg.axis().scale(scope.y).ticks(5).orient("left");

        // Power Factor Y
        var minPF = scope.min.L1_PF;
        var maxPF = 1;
        var minV = scope.min.L1_V;
        var maxV = scope.max.L1_V;

        scope.pfy = d3.scale.linear().range([scope.smallheight - marginBetween, 0]);
        scope.pfy.domain([minPF, maxPF]);
        scope.pfy.axis = d3.svg.axis().scale(scope.pfy).ticks(3).orient("left");

        scope.vy = d3.scale.linear().range([scope.smallheight - marginBetween, 0]);
        scope.vy.domain([minV, maxV]);
        scope.vy.axis = d3.svg.axis().scale(scope.vy).ticks(3).orient("left");

        if (scope.zoom) {
            scope.zoomX.axis = d3.svg.axis().scale(scope.zoomX).orient("bottom");
            scope.zoomY = d3.scale.linear().range([scope.zoomHeight - marginBetween, 0]);
            var zoomDomain = [0,1];
            scope.zoomPlotter = d3.svg.line()
                .x(function(d) { return scope.zoomX(moment(d.time).toDate()); });
            if (config.graphs.consumption) {
                // No need for the max demand here, so I use maxY alone
                zoomDomain = [minY, maxY];
                scope.zoomPlotter = d3.svg.area()
                    .x(function(d) { return scope.zoomX(moment(d.time).toDate()); })
                    .y0(function(d) { return scope.zoomY(d.net) || 0; })
                    .y1(function(d) { return (scope.zoomY(d.P || 0)) || 0; });
            } else if (config.graphs.powerfactor) {
                zoomDomain = scope.pfy.domain();
                scope.zoomPlotter.y(function(d) { return scope.zoomY(d.L1_PF || 0); });
            } else {
                zoomDomain = scope.vy.domain();
                scope.zoomPlotter.y(function(d) { return scope.zoomY(d.L1_V || 0); });
            }
            console.log(zoomDomain);
            scope.zoomY.domain(zoomDomain);
            scope.zoomY.axis = d3.svg.axis().scale(scope.zoomY).ticks(3).orient("left");
        }

        scope.linePower = d3.svg.line()
            .x(function(d) { return scope.x(moment(d.time).toDate()); })
            .y(function(d) { return scope.y(d.P || 0); });

        scope.lineSolar = d3.svg.line()
            .x(function(d) { return scope.x(moment(d.time).toDate()); })
            .y(function(d) { return scope.y(d.net); });

        scope.linePF = d3.svg.line()
            .x(function(d) { return scope.x(moment(d.time).toDate()); })
            .y(function(d) { return scope.pfy(d.L1_PF || 0); });

        scope.lineV = d3.svg.line()
            .x(function(d) { return scope.x(moment(d.time).toDate()); })
            .y(function(d) { return scope.vy(d.L1_V || 0); });

        scope.svg = d3.select(el[0]).select(".powerviewgraph").append("svg")
            .attr("width", scope.width)
            .attr("height", scope.height + scope.zoomHeight);

        scope.main = scope.svg.append("g")
            .attr("transform", "translate(" + scope.margin.left + "," + scope.margin.top + ")");

        scope.mouseRect = scope.main.append('rect')
            .attr('class', 'mouserect')
            .attr('x', 0)
            .attr('y', 0)
            .style('fill', 'none')
            .style('opacity', 1)
            .attr('width', scope.x.range()[1] - scope.x.range()[0])
            .attr('height', scope.height);

        scope.big = scope.main.append("g")
            .attr("class", "big");

        if (config.graphs) {
            scope.big.style("display", !!config.graphs.consumption? "" : "none");
        }

        var powerfactorYshift = scope.bigheight;
        if (config.graphs) {
            powerfactorYshift = !!config.graphs.consumption? scope.bigheight : 0;
        }
        scope.powerfactorSVG = scope.main.append("g")
            .attr("class", "powerfactorSVG")
            .attr("transform", "translate(0, " + powerfactorYshift + ")");

        if (config.graphs) {
            scope.powerfactorSVG.style("display", !!config.graphs.powerfactor? "" : "none");
        }

        var voltageYshift = scope.smallheight;
        if (config.graphs) {
            voltageYshift = powerfactorYshift + (!!config.graphs.powerfactor? scope.smallheight : 0);
        }
        scope.voltageSVG = scope.main.append("g")
            .attr("class", "voltageSVG")
            .attr("transform", "translate(0, " + voltageYshift + ")");

        if (config.graphs) { 
            scope.voltageSVG.style("display", !!config.graphs.voltage? "" : "none");
        }

        if (scope.zoom) {
            scope.zoomSVG = scope.main.append("g")
                .attr("class", "zoomSVG")
                .attr("transform", "translate(0, " + scope.height + ")");

            scope.zoomSVG.append("g")
                .attr("class", "x brush")
                .call(scope.brush)
                .selectAll("rect")
                .attr("y", scope.zoomY.range()[1])
                .attr("height", scope.zoomY.range()[0]);

            scope.zoomSVG.selectAll("rect.background")
                .style("visibility", "visible");
        }

        scope.main.append("defs").append("clipPath")
            .attr("id", "clip")
        .append("rect")
            .attr("width", scope.width)
            .attr("height", scope.height);

        // An area generator, for the light fill.
        scope.area = d3.svg.area()
            .x(function(d) { return scope.x(moment(d.time).toDate()); })
            .y0(function(d) { return scope.y(d.net) || 0; })
            .y1(function(d) { return scope.y(d.P || 0) || 0; });

        var xEnd = -scope.x(scope.end);

        scope.yAxis = scope.big.append("g")
            .attr("class", "y axis")
            .call(scope.y.axis.tickSize(xEnd, 0, 0));

        scope.xAxis = scope.big.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + scope.y.range()[0] + ")")
            .call(scope.x.axis = d3.svg.axis().scale(scope.x).orient("bottom"));

        scope.powerFactorXAxis = scope.powerfactorSVG.append("g")
            .attr("class", "x axis powerfactor")
            .attr("transform", "translate(0," + scope.pfy.range()[0] + ")")
            .call(scope.x.axis);

        scope.powerFactorYAxis = scope.powerfactorSVG.append("g")
            .attr("class", "y axis powerfactor")
            .call(scope.pfy.axis.tickSize(xEnd, 0, 0));

        scope.voltageXAxis = scope.voltageSVG.append("g")
            .attr("class", "x axis voltage")
            .attr("transform", "translate(0," + scope.vy.range()[0] + ")")
            .call(scope.x.axis);

        scope.voltageYAxis = scope.voltageSVG.append("g")
            .attr("class", "y axis voltage")
            .call(scope.vy.axis.tickSize(xEnd, 0, 0));

        if (scope.zoom) {
            scope.zoomXAxis = scope.zoomSVG.append("g")
                .attr("class", "x axis zoom")
                .attr("transform", "translate(0," + (scope.zoomHeight - marginBetween) + ")")
                .call(scope.x.axis);

            scope.zoomYAxis = scope.zoomSVG.append("g")
                .attr("class", "y axis zoom")
                .call(scope.vy.axis.tickSize(xEnd, 0, 0));
        }

        scope.lines = scope.big.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "lines");

        scope.powerFactorLines = scope.powerfactorSVG.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "powerfactorlines");

        scope.voltageLines = scope.voltageSVG.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "voltagelines");

        scope.hoverLineGroup = scope.main.append("g").attr("class", "hoverLine");

        scope.lineHover = scope.hoverLineGroup
            .append("line")
            .attr("class", "lineHover")
            .attr("x1", 0)
            .attr("x2", 0)
            .attr("y1", 0)
            .attr("y2", scope.height);

        scope.hoverLineGroup.style("opacity", scope.hoverLineOpacity || 1e-6);

        function mouseover() {
            scope.hoverLineOpacity = 0.9;
            scope.hoverLineGroup.style("opacity", scope.hoverLineOpacity);
            scope.tooltip.transition().duration(200).style("opacity", scope.hoverLineOpacity);
        }

        function mouseout() {
            scope.hoverLineOpacity = 1e-6;
            scope.hoverLineGroup.style("opacity", scope.hoverLineOpacity);
            scope.tooltip.transition().duration(200).style("opacity", scope.hoverLineOpacity);
        }

        scope.mousemove = function (lastPoint) {
            
            var yPoint = 0,
                xPoint = 0;

            if (!lastPoint) {
                if (!this) {
                    return;
                }
                var event = d3.mouse(this);
                if (!event) {
                    return;
                }
                xPoint = event[0];
                yPoint = event[1];
                var time = scope.x.invert(xPoint);
                var i = bisectDate(scope.data, time, 1),
                    d0 = scope.data[i - 1],
                    d1 = scope.data[i];
                if (!d0 || !d1) {
                    return;
                }
                var point = time - d0.time > d1.time - time ? d1 : d0;
                if (!point) {
                    return ;
                }
                scope.$apply(function() {
                    scope.lastPoint = point;
                });
            }
            var tooltipY = yPoint + scope.margin.top;
            var tooltipX = scope.x(moment(scope.lastPoint.time).toDate());
            scope.lineHover
                .attr('x1', tooltipX)
                .attr('x2', tooltipX);
            // 200 is the width of the tooltip box ( set in main.less )
            if ((scope.x.range()[1] - tooltipX) < 200) {
                tooltipX -= 200 - scope.margin.right;
            } else {
                tooltipX += scope.margin.left + scope.margin.left;
            }
            scope.tooltip
                .style("left", tooltipX + "px")
                .style("top", tooltipY + "px");
        };

        scope.big.append('text')
            .attr('class', 'title')
            .attr('x', scope.x.range()[1])
            .attr('y', scope.y.range()[0] - 2)
            .text('kW Demand');

        scope.powerfactorSVG.append('text')
            .attr('class', 'title')
            .attr('x', scope.x.range()[1])
            .attr('y', scope.pfy.range()[0]- 2)
            .text('Power Factor');

        scope.voltageSVG.append('text')
            .attr('class', 'title')
            .attr('x', scope.x.range()[1])
            .attr('y', scope.vy.range()[0] - 2)
            .text('Voltage');

        scope.mouseRect
            .on('mousemove', scope.mousemove)
            .on('mouseenter', mouseover)
            .on('mouseleave', mouseout);
    }

    function update(scope, data, config) {
        scope.hoverLineGroup.style("opacity", scope.hoverLineOpacity || 1e-6);

        if (scope.zoom && !scope.brush.empty()) {
            scope.x.domain(scope.brush.extent());
        } else {
            scope.x.domain([moment(scope.min.time).toDate(), moment(scope.max.time).toDate()]);
        }
        scope.start = scope.x.domain()[0];
        scope.end = scope.x.domain()[1];

        console.log("Min ", scope.min.net);
        var minY = _.min([scope.min.net, 0]);
        var maxY = _.max([scope.max.P]);
        scope.y.domain([minY, Math.max(config.maxDemand, maxY)]);

        var minPF = scope.min.L1_PF;
        var maxPF = 1;
        scope.pfy.domain([minPF, maxPF]);

        var minV = scope.min.L1_V;
        var maxV = scope.max.L1_V;
        scope.vy.domain([minV, maxV]);

        if (scope.zoom) { 
            scope.zoomY.domain([minY, maxY]);
        }

        var maxdemandLine = scope.big.select('line.maxdemand'),
            maxdemandText = scope.big.select('text.maxdemand');
        if (maxdemandLine.empty()) {
            maxdemandLine = scope.big.append('line')
                .attr("class", "maxdemand");
            maxdemandText = scope.big.append('text')
                .attr("class", "maxdemand");
        }

        maxdemandLine
            .attr("x1", scope.x(moment(scope.start).toDate()))
            .attr("x2", scope.x(moment(scope.end).toDate()))
            .attr("y1", scope.y(config.maxDemand))
            .attr("y2", scope.y(config.maxDemand));

        maxdemandText
            .attr("x", scope.x(moment(scope.end).toDate()))
            .attr("y", scope.y(config.maxDemand) + 10)
            .text(scope.config.maxDemandTitle || "Max Demand");

        // Add the area path.
        var area = scope.lines.select('path.area');
        if (area.empty()) {
            area = scope.lines.append('path')
                .attr("clip-path", "url(#clip)")
                .attr("class", "area");
        }
        area.attr("d", scope.area(data));

        // slide the x-axis left
        scope.xAxis.call(scope.x.axis.scale(scope.x));
        scope.yAxis.call(scope.y.axis.scale(scope.y));
        scope.powerFactorXAxis.call(scope.x.axis);
        scope.powerFactorYAxis.call(scope.pfy.axis.scale(scope.pfy));
        scope.voltageXAxis.call(scope.x.axis);
        scope.voltageYAxis.call(scope.vy.axis.scale(scope.vy));

        if (scope.zoom) {
            scope.zoomXAxis.call(scope.zoomX.axis.scale(scope.zoomX));
            scope.zoomYAxis.call(scope.zoomY.axis.scale(scope.zoomY));
            // Add the area path.
            var zoomGraph = scope.zoomSVG.select('path.zoomGraph');
            if (zoomGraph.empty()) {
                zoomGraph = scope.zoomSVG.append('path')
                    //.attr("clip-path", "url(#clip)")
                    .attr("class", "zoomGraph");
            }
            zoomGraph.attr("d", scope.zoomPlotter(data));
        }

        var solarLine = scope.lines.select('path.lineSolar');
        if (solarLine.empty()) {
            solarLine = scope.lines.append('path')
                .attr("clip-path", "url(#clip)")
                .attr("class", "lineSolar");
        }
        solarLine.attr("d", scope.lineSolar(data));

        var powerLine = scope.lines.select('path.linePower');
        if (powerLine.empty()) {
            powerLine = scope.lines.append('path')
                .attr("clip-path", "url(#clip)")
                .attr("class", "linePower");
        }
        powerLine.attr("d", scope.linePower(data));

        var pflines = scope.powerFactorLines.selectAll("path.linePF");
        pflines.data([data]).enter().append("path")
            .attr("class", "linePF")
            .attr("d", scope.linePF);
        pflines.attr("d", scope.linePF);
        pflines.data([data]).exit().remove();

        var vlines = scope.voltageLines.selectAll("path.lineV");
        vlines.data([data]).enter().append("path")
            .attr("class", "lineV")
            .attr("d", scope.lineV);
        vlines.attr("d", scope.lineV);
        vlines.data([data]).exit().remove();
    }

    function controller(scope, element) {

        scope.$watch('dataupdated', function() {
            if (scope.data) {
                scope.max = {
                    S: Number.MIN_VALUE,
                    P: Number.MIN_VALUE,
                    net: Number.MIN_VALUE,
                    L1_V: Number.MIN_VALUE,
                    L1_PF: Number.MIN_VALUE,
                    time: new Date(0)
                };
                scope.min = {
                    S: Number.MAX_VALUE,
                    P: Number.MAX_VALUE,
                    net: Number.MAX_VALUE,
                    L1_V: Number.MAX_VALUE,
                    L1_PF: Number.MAX_VALUE,
                    time: new Date()
                };

                // Single loop to get them all, single ring to role them all :D
                _.each(scope.data, function(d) {
                    d.net = d.P - d.S;
                    scope.max.S = scope.max.S < d.S ? d.S : scope.max.S; 
                    scope.max.P = scope.max.P < d.P ? d.P : scope.max.P; 
                    scope.max.net = scope.max.net < d.net ? d.net : scope.max.net; 
                    scope.max.L1_V = scope.max.L1_V < d.L1_V ? d.L1_V : scope.max.L1_V; 
                    scope.max.L1_PF = scope.max.L1_PF < d.L1_PF ? d.L1_PF : scope.max.L1_PF; 
                    scope.max.time = scope.max.time < d.time ? d.time : scope.max.time; 

                    scope.min.S = scope.min.S > d.S ? d.S : scope.min.S; 
                    scope.min.P = scope.min.P > d.P ? d.P : scope.min.P; 
                    scope.min.net = scope.min.net > d.net ? d.net : scope.min.net; 
                    scope.min.L1_V = scope.min.L1_V > d.L1_V ? d.L1_V : scope.min.L1_V; 
                    scope.min.L1_PF = scope.min.L1_PF > d.L1_PF ? d.L1_PF : scope.min.L1_PF; 
                    scope.min.time = scope.min.time > d.time ? d.time : scope.min.time; 
                    // Filter based on P & S
                    return d.P && d.S && d.L1_V && d.L1_PF;
                });

                //scope.data = _.sortBy(scope.data, 'time');

                scope.config.maxDemand = parseInt(scope.config.maxDemand) || _.max([scope.max.S, scope.max.P]);

                scope.tooltip = d3.select(element[0])
                    .select("div.tooltip")
                    .style("opacity", scope.hoverLineOpacity || 1e-6);

                if (scope.svg) {
                    update(scope, scope.data, scope.config);
                    if (scope.lastPoint) {
                        scope.mousemove(scope.lastPoint);
                    }
                } else {
                    scope.time = scope.max.time;
                    plot(scope, element, scope.data, scope.config);
                    update(scope, scope.data, scope.config);
                }
            }
        });
    }

    angular.module('insightApp')
    .directive('powergraph', function () {
        return {
            templateUrl: 'views/directives/powergraph.html',
            replace: true,
            restrict: 'E',
            scope: {
                data: '=',
                config: '=',
                dataupdated: '@',
                maxDemand: '@',
                zoom: '='
            },
            controller: ['$scope', '$element', controller]
        };
    });

}).call(null);
