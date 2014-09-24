/* jshint quotmark: false */
/* global d3, _ */
'use strict';

(function() {

    var duration = 4900;
    var marginBetween = 30;
    function plot(scope, el, data, maxDemand) {

        if (!data || !data.length) {
            return;
        }

        scope.start = _.min(data, 'time').time;
        scope.end = _.max(data, 'time').time;

        scope.margin = {top: 6, right: 0, bottom: 20, left: 40};
        scope.width = el.width() - scope.margin.right - scope.margin.left;
        scope.height = el.height() - scope.margin.top - scope.margin.bottom;
        scope.bigheight = scope.height / 2;
        scope.smallheight = (scope.height / 4) - (2 * marginBetween);

        scope.x = d3.time.scale().range([0, scope.width]);
        scope.x.domain([scope.start, scope.end]);

        scope.y = d3.scale.linear().range([scope.bigheight, 0]);
        scope.y.domain([0, maxDemand + 20]);
        scope.y.axis = d3.svg.axis().scale(scope.y).ticks(5).orient("left");

        // Power Factor Y
        var minPF = _.min(data, 'L1_PF').L1_PF - 0.1;
        //var maxPF = _.max(data, 'L1_PF').L1_PF + 0.1;
        var maxPF = 1;
        var minV = _.min(data, 'L1_V').L1_V - 5;
        var maxV = _.max(data, 'L1_V').L1_V + 5;

        scope.pfy = d3.scale.linear().range([scope.smallheight, 0]);
        scope.pfy.domain([minPF, maxPF]);
        scope.pfy.axis = d3.svg.axis().scale(scope.pfy).ticks(3).orient("left");

        scope.vy = d3.scale.linear().range([scope.smallheight, 0]);
        scope.vy.domain([minV, maxV]);
        scope.vy.axis = d3.svg.axis().scale(scope.vy).ticks(3).orient("left");

        scope.linePower = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.y(d.P); });

        scope.lineSolar = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.y(d.P - d.S); });

        scope.linePF = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.pfy(d.L1_PF); });

        scope.lineV = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.vy(d.L1_V); });

        scope.svg = d3.select(el[0]).select(".graph").append("svg")
            .attr("width", scope.width + scope.margin.left + scope.margin.right)
            .attr("height", scope.height + scope.margin.top + scope.margin.bottom);

        scope.mouseRect = scope.svg.append('rect')
            .attr('x', scope.x.range()[0])
            .attr('y', 0)
            .style('fill', 'blue')
            .style('opacity', 1)
            .attr('width', scope.x.range()[1] - scope.x.range[0])
            .attr('height', scope.margin.top + scope.height);

        scope.big = scope.svg.append("g")
            .attr("class", "big")
            .attr("transform", "translate(" + scope.margin.left + "," + scope.margin.top + ")");

        scope.powerfactorSVG = scope.svg.append("g")
            .attr("class", "powerfactorSVG")
            .attr("transform", "translate(" + scope.margin.left + "," + (scope.margin.top + scope.bigheight + marginBetween) + ")");

        scope.voltageSVG = scope.svg.append("g")
            .attr("class", "voltageSVG")
            .attr("transform", "translate(" + scope.margin.left + "," + (scope.margin.top + scope.bigheight + scope.smallheight + (2 * marginBetween) ) + ")");

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

        /**
         * Formats a single entry in the tooltip
         */
        function formatEntry(key, value) {
            var html = '<div class="entry">';
            html += '<span class="left">' + key + '</span>';
            html += '<span class="right">' + value + '</span>';
            html += "</div>";
            return html;
        }

        /**
         * Sets the tooltip html content with the data relative to the passed
         * point
         */
        function setTooltip(point) {
            var html = '';
            html += formatEntry('Price', '$' + point.price.toFixed(2));
            html += formatEntry('ROM', (point.payout / data.margin).toFixed(2) + "%");
            html += formatEntry('Prob >', (1 - point.cdf).toFixed(2) + "%");
            html += formatEntry('Prob <', point.cdf.toFixed(2) + "%");
            html += formatEntry('SD', ((point.price - data.forecast) / data.sd).toFixed(2));
            scope.tooltip.html(html);
            scope.tooltip.transition().duration(200).style("opacity", 0.9);
        }

        function mouseover() {
            scope.hoverLineGroup.style("opacity", "1");
        }

        function mouseout() {
            scope.hoverLineGroup.style("opacity", 1e-6);
            scope.tooltip.transition()
                .duration(200)
                .style("opacity", 0);
        }

        function mousemove(d) {
            if (!d3.event) {
                return;
            }
            var xPoint = d3.mouse(scope.svg.node())[0];
            var time = scope.x.invert(xPoint);
            //var point = findNearestPoint(price);
            //hoverLineGroup.attr('transform', 'translate(' + (scope.x(point.price) + margin.left) + ', 0)');
            //setTooltip(point);

            //tooltip.style("left", (d3.event.pageX + 10) + "px")
            //.style("top", (d3.event.pageY - 28) + "px");
        }

        scope.mouseRect.on('mousemove', mousemove)
            .on('mouseover', mouseover)
            .on('mouseout', mouseout);

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
    }

    function update(scope, data, maxDemand) {

        scope.start = _.min(data, 'time').time;
        scope.end = _.max(data, 'time').time;

        scope.x.domain([scope.start, scope.end]);
        scope.y.domain([0, maxDemand + 20]);

        var minPF = _.min(data, 'L1_PF').L1_PF - 0.1;
        var maxPF = _.max(data, 'L1_PF').L1_PF + 0.1;
        scope.pfy.domain([minPF, maxPF]);

        var minV = _.min(data, 'L1_V').L1_V - 5;
        var maxV = _.max(data, 'L1_V').L1_V + 5;
        scope.vy.domain([minV, maxV]);

        scope.lines.selectAll("path").attr("transform", null);

        var maxdemandLine = scope.lines.select('line.maxdemand');
        if (maxdemandLine.empty()) {
            maxdemandLine = scope.lines.append('line')
                .attr("class", "maxdemand");
        }
        maxdemandLine
            .attr("x1", scope.x(scope.start))
            .attr("x2", scope.x(scope.end))
            .attr("y1", scope.y(maxDemand))
            .attr("y2", scope.y(maxDemand));

        // Add the area path.
        var area = scope.lines.select('path.area');
        if (area.empty()) {
            area = scope.lines.append('path')
                .attr("class", "area");
        }
        area.attr("clip-path", "url(#clip)")
            .attr("d", scope.area(data));

        // slide the x-axis left
        scope.xAxis.call(scope.x.axis);
        scope.powerFactorXAxis.call(scope.x.axis);
        scope.voltageXAxis.call(scope.x.axis);

        //var oldTime = _.min(allData, 'time').time;
        var solarLines = scope.lines.selectAll("path.lineSolar");
        solarLines.data([data]).enter().append("path")
            .attr("class", "lineSolar")
            .attr("d", scope.lineSolar);
        solarLines.attr("d", scope.lineSolar);
        solarLines.data([data]).exit().remove();

        var powerLines = scope.lines.selectAll("path.linePower");
        powerLines.data([data]).enter().append("path")
            .attr("class", "linePower")
            .attr("d", scope.linePower);
        powerLines.attr("d", scope.linePower);
        powerLines.data([data]).exit().remove();

            // slide the line left
            //path.transition()
                //.attr("transform", "translate(" + x(now - (n - 1) * duration) + ")")
                //.each("end", tick);

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
        scope.$watch('data', function() {
            if (scope.data) {
                var maxDemand = parseInt(scope.maxDemand) || _.max([_.max(scope.data, 'S').S, _.max(scope.data, 'P').P]);

                scope.tooltip = d3.select(element[0])
                    .select("div.tooltip")
                    .style("opacity", 0);

                if (scope.svg) {
                    update(scope, scope.data, maxDemand);
                } else {
                    scope.time = _.max(scope.data, 'time').time;
                    plot(scope, element, scope.data, maxDemand);
                }
            }
        });
    }

    angular.module('insightApp')
    .directive('powergraph', function () {
        return {
            template: '<div><div class="tooltip"></div><div class="graph" style="height: 500px"></div></div>',
            replace: true,
            restrict: 'E',
            scope: {
                data: '=',
                maxDemand: '@',
            },
            controller: ['$scope', '$element', controller]
        };
    });

}).call(null);
