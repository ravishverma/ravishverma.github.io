"use strict";

d3.select('body')
.insert('div','script#headerScript+*').attr('id','logo')
.append('center')
.append('h1')
.text('RAVISH VERMA');

var navigate = d3.select('body')
.insert('div','div#logo+*').attr('id','navigate')
.append('center');

navigate.append('a').attr('href','/main.html').text('Home\t');
navigate.append('a').attr('href','/travellogs/travellogs.html').text('TravelLogs\t');
navigate.append('a').attr('href','/health/health.html').text('Health\t');
navigate.append('a').attr('href','/projects/projects.html').text('Projects\t');
navigate.append('a').attr('href','/main.html').text('Contact');

document.getElementsByTagName('body')[0].insertBefore(document.createElement('hr'),document.getElementById('navigate'));

document.getElementById('navigate').after(document.createElement('hr'));
