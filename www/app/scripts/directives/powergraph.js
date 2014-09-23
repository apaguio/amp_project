/* jshint quotmark: false */
/* global d3, _ */
'use strict';

(function() {

    var duration = 4900;
    function plot(scope, el, data, maxDemand) {

        if (!data || !data.length) {
            return;
        }

        scope.margin = {top: 6, right: 0, bottom: 20, left: 40};
        scope.width = el.width() - scope.margin.right - scope.margin.left;
        scope.height = el.height() - scope.margin.top - scope.margin.bottom;

        scope.x = d3.time.scale()
            .range([0, scope.width]);

        scope.y = d3.scale.linear()
            .range([scope.height, 0]);

        scope.linePower = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.y(d.P); });

        scope.lineSolar = d3.svg.line()
            //.interpolate("basis")
            .x(function(d) { return scope.x(d.time); })
            .y(function(d) { return scope.y(d.P - d.S); });

        scope.svg = d3.select(el[0]).append("svg")
            .attr("width", scope.width + scope.margin.left + scope.margin.right)
            .attr("height", scope.height + scope.margin.top + scope.margin.bottom)
        .append("g")
            .attr("transform", "translate(" + scope.margin.left + "," + scope.margin.top + ")");

        scope.svg.append("defs").append("clipPath")
            .attr("id", "clip")
        .append("rect")
            .attr("width", scope.width)
            .attr("height", scope.height);

        scope.xAxis = scope.svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + scope.height + ")")
            .call(scope.x.axis = d3.svg.axis().scale(scope.x).orient("bottom"));

        scope.lines = scope.svg.append("g")
            .attr("clip-path", "url(#clip)")
            .attr("class", "lines");
    }

    function update(scope, data, maxDemand) {

        scope.start = _.min(data, 'time').time;
        scope.end = _.max(data, 'time').time;

        scope.x.domain([scope.start, scope.end]);
        scope.y.domain([0, maxDemand]);

        scope.lines.selectAll("path").attr("transform", null);

        // slide the x-axis left
        scope.xAxis
            //.transition()
            //.duration(duration)
            //.ease("linear")
            .call(scope.x.axis);

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

        var powerLines = scope.lines.selectAll("path.linePower")
            
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
    }

    function controller(scope, element) {
        scope.$watch('data', function() {
            if (scope.data) {
                var maxDemand = scope.maxDemand || _.max([_.max(scope.data, 'S').S, _.max(scope.data, 'P').P]);
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
