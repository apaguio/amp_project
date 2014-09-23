'use strict';

(function() {

    function plot(el, data, maxDemand) {

        if (!data || !data.length) {
            return;
        }

        var margin = {top: 6, right: 0, bottom: 20, left: 40},
            width = el.width() - margin.right - margin.left,
            height = el.height() - margin.top - margin.bottom;

        var start = _.min(data, 'time').time,
            end = _.max(data, 'time').time;

        var x = d3.time.scale()
            .domain([start, end])
            .range([0, width]);

        var y = d3.scale.linear()
            .domain([0, maxDemand])
            .range([height, 0]);

        var linePower = d3.svg.line()
            //.interpolate("basis")
            .x(function(d, i) { return x(d.time); })
            .y(function(d, i) { return y(d.P); });

        var lineSolar = d3.svg.line()
            //.interpolate("basis")
            .x(function(d, i) { return x(d.time); })
            .y(function(d, i) { return y(d.S); });

        var svg = d3.select(el[0]).append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .style("margin-left", -margin.left + "px")
        .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        //svg.append("defs").append("clipPath")
            //.attr("id", "clip")
        //.append("rect")
            //.attr("width", width)
            //.attr("height", height);

        var axis = svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(x.axis = d3.svg.axis().scale(x).orient("bottom"));

        var lines = svg.append("g")
            //.attr("clip-path", "url(#clip)")
            .attr("class", "lines");

        lines.append("path")
            .data([data])
            .attr("class", "lineSolar")
            .attr("d", lineSolar);

        lines.append("path")
            .data([data])
            .attr("class", "linePower")
            .attr("d", linePower);

        //tick();

        //d3.select(window)
            //.on("scroll", function() { ++count; });

        function tick() {

            // update the domains
            now = new Date();
            x.domain([now - (n - 2) * duration, now - duration]);
            y.domain([0, d3.max(data)]);

            // push the accumulated count onto the back, and reset the count
            data.push(Math.min(30, count));
            count = 0;

            // redraw the line
            svg.select(".line")
                .attr("d", line)
                .attr("transform", null);

            // slide the x-axis left
            axis.transition()
                .duration(duration)
                .ease("linear")
                .call(x.axis);

            // slide the line left
            path.transition()
                .duration(duration)
                .ease("linear")
                .attr("transform", "translate(" + x(now - (n - 1) * duration) + ")")
                .each("end", tick);

            // pop the old data point off the front
            data.shift();

        }

    }

    function postLink(scope, element, attrs) {
        scope.$watch('data', function() {
            if (scope.data) {
                var c = scope.data.data.consumption;
                var s = scope.data.data.solar;
                var points = _.map(c.points, function(p, i) {
                    var consumedPoint = _.zipObject(c.columns, p);
                    var solarPoint = _.zipObject(s.columns, s.points[i]);
                    //  Add the solar saved power to the consumed point
                    consumedPoint.S = solarPoint.P;
                    consumedPoint.time *= 1000;
                    return consumedPoint;
                });
                plot(element, points, scope.max_demand || _.max([_.max(points, 'S').S, _.max(points, 'P').P]) );
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
            link: postLink
        };
    });

}).call(null);
