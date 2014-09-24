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
        scope.bigheight = scope.height * 2 / 3;
        scope.smallheight = (scope.height / 3) - marginBetween;

        scope.x = d3.time.scale().range([0, scope.width]);
        scope.x.domain([scope.start, scope.end]);

        scope.y = d3.scale.linear().range([scope.bigheight, 0]);
        scope.y.domain([0, maxDemand + 20]);
        scope.y.axis = d3.svg.axis().scale(scope.y).ticks(5).orient("left");

        // Power Factor Y
        var minPF = _.min(data, 'L1_PF').L1_PF - 0.1;
        var maxPF = _.max(data, 'L1_PF').L1_PF + 0.1;
        scope.pfy = d3.scale.linear().range([scope.smallheight, 0]);
        scope.pfy.domain([minPF, maxPF]);
        scope.pfy.axis = d3.svg.axis().scale(scope.pfy).ticks(5).orient("left");

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

        scope.svg = d3.select(el[0]).append("svg")
            .attr("width", scope.width + scope.margin.left + scope.margin.right)
            .attr("height", scope.height + scope.margin.top + scope.margin.bottom);

        scope.big = scope.svg.append("g")
            .attr("class", "big")
            .attr("transform", "translate(" + scope.margin.left + "," + scope.margin.top + ")");

        scope.small = scope.svg.append("g")
            .attr("class", "small")
            .attr("transform", "translate(" + scope.margin.left + "," + (scope.margin.top + scope.bigheight + marginBetween) + ")");

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
            .attr("class", "x axis")
            .call(scope.y.axis);

        scope.xAxis = scope.big.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + scope.bigheight + ")")
            .call(scope.x.axis = d3.svg.axis().scale(scope.x).orient("bottom"));

        scope.smallXAxis = scope.small.append("g")
            .attr("class", "x axis small")
            .attr("transform", "translate(0," + scope.smallheight + ")")
            .call(scope.x.axis);

        scope.pfyAxis = scope.small.append("g")
            .attr("class", "x axis")
            .call(scope.pfy.axis);

        scope.lines = scope.big.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "lines");

        scope.pflines = scope.small.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "pflines");
    }

    function update(scope, data, maxDemand) {

        scope.start = _.min(data, 'time').time;
        scope.end = _.max(data, 'time').time;

        scope.x.domain([scope.start, scope.end]);
        scope.y.domain([0, maxDemand + 20]);
        var minPF = _.min(data, 'L1_PF').L1_PF - 0.1;
        var maxPF = _.max(data, 'L1_PF').L1_PF + 0.1;

        scope.pfy.domain([minPF, maxPF]);

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
        scope.xAxis
            //.transition()
            //.duration(duration)
            //.ease("linear")
            .call(scope.x.axis);

        scope.smallXAxis.call(scope.x.axis);

        //var oldTime = _.min(allData, 'time').time;
        var solarLines = scope.lines.selectAll("path.lineSolar");
        solarLines.data([data]).enter().append("path")
            .attr("class", "lineSolar")
            .attr("d", scope.lineSolar);

        solarLines.attr("d", scope.lineSolar);
            //.transition()
            //.duration(duration)
            //.ease("linear")
            //.attr("transform", "translate(" + scope.x(oldTime) + ")");
        solarLines.data([data]).exit().remove();

        var powerLines = scope.lines.selectAll("path.linePower");
            
        powerLines.data([data]).enter().append("path")
            .attr("class", "linePower")
            .attr("d", scope.linePower);
        powerLines
            .attr("d", scope.linePower);
            //.transition()
            //.duration(duration)
            //.ease("linear")
            //.attr("transform", "translate(" + scope.x(oldTime) + ")");
        powerLines.data([data]).exit().remove();

            // slide the line left
            //path.transition()
                //.attr("transform", "translate(" + x(now - (n - 1) * duration) + ")")
                //.each("end", tick);

        var pflines = scope.pflines.selectAll("path.linePF");
            
        pflines.data([data]).enter().append("path")
            .attr("class", "linePF")
            .attr("d", scope.linePF);
        pflines
            .attr("d", scope.linePF);
            //.transition()
            //.duration(duration)
            //.ease("linear")
            //.attr("transform", "translate(" + scope.x(oldTime) + ")");
        pflines.data([data]).exit().remove();

    }

    function controller(scope, element) {
        scope.$watch('data', function() {
            if (scope.data) {
                var maxDemand = parseInt(scope.maxDemand) || _.max([_.max(scope.data, 'S').S, _.max(scope.data, 'P').P]);
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
            template: '<div style="height: 500px"></div>',
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
