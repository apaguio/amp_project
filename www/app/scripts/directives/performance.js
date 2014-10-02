/* jshint quotmark: false */
/* global d3, _ */
'use strict';

(function() {

    var duration = 4900;
    var marginBetween = 30;
    var bisectDate = d3.bisector(function(d) { return d.time; }).left;
    function plot(scope, el, data, maxDemand) {

        if (!data || !data.length) {
            return;
        }

        scope.yBegining = el[0].getBoundingClientRect().top;
        scope.start = scope.min.time;
        scope.end = scope.max.time;

        scope.margin = {top: 6, right: 0, bottom: 20, left: 40};
        scope.width = el.width() - scope.margin.right - scope.margin.left;
        scope.height = el.height() - scope.margin.top - scope.margin.bottom;
        scope.bigheight = scope.height / 2;
        scope.smallheight = (scope.height / 4) - (2 * marginBetween);

        scope.x = d3.time.scale().range([0, scope.width - scope.margin.left - scope.margin.right]);
        scope.x.domain([scope.start, scope.end]);

        scope.y = d3.scale.linear().range([scope.bigheight, 0]);
        scope.y.domain([0, maxDemand + 20]);
        scope.y.axis = d3.svg.axis().scale(scope.y).ticks(5).orient("left");


        // Power Factor Y
        var minPF = scope.min.L1_PF - 0.1;
        //var maxPF = _.max(data, 'L1_PF').L1_PF + 0.1;
        var maxPF = 1;
        var minV = scope.min.L1_V - 5;
        var maxV = scope.max.L1_V + 5;

        scope.pfy = d3.scale.linear().range([scope.smallheight, 0]);
        scope.pfy.domain([minPF, maxPF]);
        scope.pfy.axis = d3.svg.axis().scale(scope.pfy).ticks(3).orient("left");

        scope.vy = d3.scale.linear().range([scope.smallheight, 0]);
        scope.vy.domain([minV, maxV]);
        scope.vy.axis = d3.svg.axis().scale(scope.vy).ticks(3).orient("left");

        scope.linePower = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.y(d.P || 0); });

        scope.lineSolar = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.y( (d.P || 0) - (d.S || 0 ) ); });

        scope.linePF = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.pfy(d.L1_PF || 0); });

        scope.lineV = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.vy(d.L1_V || 0); });

        scope.svg = d3.select(el[0]).select(".graph").append("svg")
            .attr("width", scope.width + scope.margin.left + scope.margin.right)
            .attr("height", scope.height + scope.margin.top + scope.margin.bottom);

        scope.mouseRect = scope.svg.append('rect')
            .attr('class', 'mouserect')
            .attr('x', scope.margin.left)
            .attr('y', scope.margin.top)
            .style('fill', 'none')
            .style('opacity', 1)
            .attr('width', scope.x.range()[1] - scope.x.range()[0])
            .attr('height', scope.margin.top + scope.height);

        scope.big = scope.svg.append("g")
            .attr("class", "big")
            .attr("transform", "translate(" + scope.margin.left + "," + scope.margin.top + ")");

        scope.grid = scope.big.append("g")
            .attr("class", "grid");

        scope.powerfactorSVG = scope.svg.append("g")
            .attr("class", "powerfactorSVG")
            .attr("transform", "translate(" + scope.margin.left + "," + (scope.margin.top + scope.bigheight + marginBetween) + ")");

        scope.pfgrid = scope.powerfactorSVG.append("g")
            .attr("class", "pfgrid");

        scope.voltageSVG = scope.svg.append("g")
            .attr("class", "voltageSVG")
            .attr("transform", "translate(" + scope.margin.left + "," + (scope.margin.top + scope.bigheight + scope.smallheight + (2 * marginBetween) ) + ")");

        scope.voltageGrid = scope.voltageSVG.append("g")
            .attr("class", "vgrid");

        scope.svg.append("defs").append("clipPath")
            .attr("id", "clip")
        .append("rect")
            .attr("width", scope.width)
            .attr("height", scope.height);

        // An area generator, for the light fill.
        scope.area = d3.svg.area()
            //.interpolate("monotone")
            .x(function(d) { return scope.x(d.time); })
            .y0(function(d) { return scope.y((d.P || 0) - (d.S || 0)); })
            .y1(function(d) { return scope.y(d.P || 0); });

        scope.yAxis = scope.big.append("g")
            .attr("class", "y axis")
            .call(scope.y.axis);

        scope.gridYAxis = scope.grid.append("g")
            .attr("class", "gridyaxis")
            .call(scope.y.axis.tickSize(-scope.x(scope.end), 0, 0).tickFormat(""));

        scope.xAxis = scope.big.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + scope.bigheight + ")")
            .call(scope.x.axis = d3.svg.axis().scale(scope.x).orient("bottom"));

        scope.powerFactorXAxis = scope.powerfactorSVG.append("g")
            .attr("class", "x axis powerfactor")
            .attr("transform", "translate(0," + scope.smallheight + ")")
            .call(scope.x.axis);

        scope.voltageXAxis = scope.voltageSVG.append("g")
            .attr("class", "x axis voltage")
            .attr("transform", "translate(0," + scope.smallheight + ")")
            .call(scope.x.axis);

        scope.powerFactorYAxis = scope.powerfactorSVG.append("g")
            .attr("class", "y axis powerfactor")
            .call(scope.pfy.axis);

        scope.voltageYAxis = scope.voltageSVG.append("g")
            .attr("class", "y axis voltage")
            .call(scope.vy.axis);

        scope.lines = scope.big.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "lines");

        scope.powerFactorLines = scope.powerfactorSVG.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "powerfactorlines");

        scope.voltageLines = scope.voltageSVG.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "voltagelines");

        scope.hoverLineGroup = scope.svg.append("g").attr("class", "hoverLine");

        scope.lineHover = scope.hoverLineGroup
            .append("line")
            .attr("class", "lineHover")
            .attr("x1", 0)
            .attr("x2", 0)
            .attr("y1", 0)
            .attr("y2", scope.height );

        scope.hoverLineGroup.style("opacity", 1e-6);

        function mouseover() {
            scope.hoverLineGroup.style("opacity", "1");
        }

        function mouseout() {
            scope.lastMouseMoveD = null;
            scope.hoverLineGroup.style("opacity", 1e-6);
            scope.tooltip.style("opacity", 0);
        }

        var lastPoint = null;
        var findNearestPoint = _.memoize(function (time) {
            time = time.setMilliseconds(0);
            var point = _.find(scope.data, {time: time});
            if (!point) {
                point = lastPoint;
            }
            lastPoint = point;
            return point;
        });

        scope.mousemove = function (d) {
            var event = d3.mouse(this);
            if (!event) {
                return;
            }
            scope.lastMouseMoveD = d;
            var xPoint = event[0];
            var yPoint = event[1];
            var time = scope.x.invert(xPoint - scope.margin.left);
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
            var xVal = scope.x(point.time);
            scope.lineHover
                .attr('x1', xVal + scope.margin.left)
                .attr('x2', xVal + scope.margin.left);

            scope.tooltip.transition().duration(200).style("opacity", 0.9);
            var tooltipY = yPoint - scope.yBegining + scope.margin.top;
            scope.tooltip
                .style("left", function(d) {
                    xVal += scope.margin.left;
                    if ((scope.x.range()[1] - xVal) < 150) {
                        // subtract value should equal the tooltip width in css
                        xVal -= 160;
                    } else {
                        xVal += scope.margin.left;
                    }
                    return xVal + "px";
                })
                .style("top", tooltipY + "px");
            scope.$apply(function() {
                scope.currentPoint = point;
            });
        };

        scope.big.append('text')
            .attr('class', 'title')
            .attr('x', scope.x.range()[1])
            .attr('y', scope.y.range()[0] - 2)
            .text('kW Demand');

        scope.powerfactorSVG.append('text')
            .attr('class', 'title')
            .attr('x', scope.x.range()[1])
            .attr('y', scope.pfy.range()[0] - 2)
            .text('Power Factor');

        scope.voltageSVG.append('text')
            .attr('class', 'title')
            .attr('x', scope.x.range()[1])
            .attr('y', scope.vy.range()[0] - 2)
            .text('Voltage');

        scope.mouseRect
            .on('mousemove', scope.mousemove)
            .on('mouseenter', mouseover)
            .on('mouseout', mouseout);
    }

    function update(scope, data, maxDemand) {

        $('svg').mousemove();
        scope.start = scope.min.time;
        scope.end = scope.max.time;

        scope.x.domain([scope.start, scope.end]);
        scope.y.domain([0, maxDemand + 20]);

        var minPF = scope.min.L1_PF - 0.1;
        var maxPF = scope.max.L1_PF + 0.1;
        scope.pfy.domain([minPF, maxPF]);

        var minV = scope.min.L1_V - 5;
        var maxV = scope.max.L1_V + 5;
        scope.vy.domain([minV, maxV]);

        //scope.lines.selectAll("path").attr("transform", null);

        var maxdemandLine = scope.big.select('line.maxdemand'),
            maxdemandText = scope.big.select('text.maxdemand');
        if (maxdemandLine.empty()) {
            maxdemandLine = scope.big.append('line')
                .attr("class", "maxdemand");
            maxdemandText = scope.big.append('text')
                .attr("class", "maxdemand");
        }
        maxdemandLine
            .attr("x1", scope.x(scope.start))
            .attr("x2", scope.x(scope.end))
            .attr("y1", scope.y(maxDemand))
            .attr("y2", scope.y(maxDemand));

        maxdemandText
            .attr("x", scope.x(scope.end))
            .attr("y", scope.y(maxDemand) + 10)
            .text("Max Demand");

        // Add the area path.
        var area = scope.lines.select('path.area');
        if (area.empty()) {
            area = scope.lines.append('path')
                .attr("clip-path", "url(#clip)")
                .attr("class", "area");
        }
        area.attr("d", scope.area(data));

        // slide the x-axis left
        scope.xAxis.call(scope.x.axis);
        scope.powerFactorXAxis.call(scope.x.axis);
        scope.voltageXAxis.call(scope.x.axis);

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
                debugger; 
                plot(scope, element, scope.data);
            }
        });
    }

    angular.module('insightApp')
    .directive('performancegraph', function () {
        return {
            templateUrl: 'views/directives/performancegraph.html',
            replace: true,
            restrict: 'E',
            scope: {
                data: '=',
                dataupdated: '@'
            },
            controller: ['$scope', '$element', controller]
        };
    });

}).call(null);
