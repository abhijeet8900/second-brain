# Enterprise Dashboard - Sprih

Created: March 8, 2024 10:22 PM

## Problem Statement :

Create an Enterprise grade software dashboard using React client-side rendering, JS, CSS/tailwind which contains:

- Widgets such as bar charts, pie charts, etc. which visualize the data in different formats.
- Ensure that the dashboard should be of enterprise quality and production standard.

## Requirement Questions :

- What is enterprise domain we are building dashboard for ? which type of dashboard we are creating ? eg **Strategic, Analytical, Operational, Tactical.**
    - Example of complex process data
    - bar chart pie charts
    - eg 4 companies, which has better revenue and which is doing better.
    - mocky, 123api, twitter
- Do we have sample design for required dashboard
    - use online design
- What are key KPI’s / data we want to show on dashboard ?
    - decide according to data.
    - look for company related data. what kind of data companies release which can be visualized
- ~~Apart from charts what other visualizations widgets we need ?~~
- Which kind of widgets and Charts we want to show for each KPI / data ?
    - Overviw : BarChart.
    - PieChart ( display certain information ). aggregation
    - List of data : barchart
- ~~How many widgets we need to show ?~~
- ~~Does widget needs to be customizable ? what are requirements around its customization ? ( Eg name can be updated )~~
- ~~Is there currently a data source? If not, what does the ideal data source look like?~~
- ~~Apart from dashboard are there any pages ? If yes, which and what are requirements for these pages ? Do we have any navigation component ? eg navbar.~~
- Is there any customization requirements around dashboard ? if yes what are those ?
    - variations in widget. should be flexible with more data
    - no requirement dashboard, widget
    
- ~~Are there any role and user restrictions on dashboard ?~~
- Is there any specific requirements around dashboard and charts interactivity ?
    - ~~Behavior around legends. Eg on hover, show / hide~~
    - ~~if user hovers over data points ?~~
    - ~~Any widget with filter option~~
    - on hover user should see more info about indicator
    
- Do we have any specific requirements around data drilling for charts and widgets we are showing ?
    - if we can yes.
- ~~Is there any specific color theme that needs to be followed ?~~
- ~~Is there any requirement around which font we need to use ?~~
- Does we need to implement and functionality around exporting charts ?
    - No

## Technical Questions :

- What are requirements for dashboard on different device ?
    - make mobile version.
- Does dashboard has to be responsive ? ~~If yes which devices we need to support and what are there width ranges ( eg. 360px - 1024px mobile )~~
- ~~Any device specific dashboard considerations ? eg Vertically stack charts on mobile ?~~
- ~~Do we need to use any specific visualization library eg ( chat.js, d3 )~~
- If we have data source does data need to be updated real-time ? or we want to update data at particular interval ? what is time interval ?
    - only when page loads
- ~~What are behavior when we have errors on dashboard ? eg no data available, API fails~~
- Are there any specific requirements around performance of application ?
    - best practices for tech stack
    - it should scale horizontally, vertically
    - if bars doen’t fit viewport if should handle that
    - change in company

- Does project needs to be hosted ?
    - No, only if possible
- Does project need to use typescript ?
    - 
- Does we need to use Rest API or GraphQL to get data from data source
- Can we use any React UI library for dashboard and widgets
    - d3
    - no preference
- Optional - Navbar
- Zoom in zoom out

## Tasks :

- [ ]  Project Setup
    - [x]  Create repository
    - [x]  Setup react with vite,
    - [x]  tailwind,
    - [ ]  Unit testing [optional]
    - [ ]  Wrapper for API client
    - [ ]  Setup env file
- [ ]  Find Public API
    - [ ]  Should have large data
    - [ ]  Should have complex data
    - [ ]  Data related to companies
- [ ]  Decide what charts we can implement to which represent data
    - [ ]  Charts should be work on mobile as well
    - [ ]  Should have inbuilt interactivity features
    - [ ]  Should have ability to zoom
- [x]  Library research and confirmation
    - [x]  Library for rendering charts
        - [https://www.chartjs.org](https://www.chartjs.org/) ( [https://react-chartjs-2.js.org/examples](https://react-chartjs-2.js.org/examples) )
    - [ ]  ~~Libraries which can be used for UI components~~
    - [ ]  ~~Library for API Client~~
- [x]  Install and Setup Charts Library
- [x]  Design Research and finalization
    - Options
        1. [https://madewithreactjs.com/mosaic-lite](https://madewithreactjs.com/mosaic-lite)
        2. [https://madewithreactjs.com/shards-dashboard-lite-react](https://madewithreactjs.com/shards-dashboard-lite-react)
        3. [https://dribbble.com/shots/22991020-Revenue-Performance-Dashboard](https://dribbble.com/shots/22991020-Revenue-Performance-Dashboard)
    - [x]  Finalize Option ( 1
- [x]  Divide design into components
    - [x]  Components should be reusable
    - [x]  Should be open to change, customizable using props
- [x]  Setup dashboard layout
- [x]  Create Chart Components
    - [x]  Bar Chart
    - [x]  Polar Area Chart
    - [x]  Pie Chart / Doughnut Chart
    - [x]  Horizontal Bar Chart
    - [x]  Line Chart
- [x]  Remove Last Chart
- [x]  Update Fonts
- [x]  Remove background grids from chart
- [x]  Rename chart headers
- [x]  Setup API Client
- [x]  Setup mock API’s
- [x]  Call endpoint to get data
- [ ]  Global transformer for data to chart structure
- [ ]  Trim dataset with Top 10 companies
    - [ ]  Add mock data where needed
        - [x]  Add random financial stages for compnay if unknown
        - [ ]  Lower valuation for ByteDance, Stripe
        - [ ]  Aggregate Industries
- [x]  Add X and Y axis label where needed.
- [x]  Remove legend if only 1
- [x]  Zoom more on legend hover
- [ ]  Add card component to show values
- [ ]  ~~Update styles for page header~~
- [x]  Add loading states for card
- [ ]  Add error handling
    - [ ]  in API client
    - [ ]  component
- [x]  Add colors for charts
- [ ]  Make legends scrollable
- [x]  Adding navbar
- [ ]  Char JS libarary optimization ( [https://www.chartjs.org/docs/latest/getting-started/integration.html](https://www.chartjs.org/docs/latest/getting-started/integration.html) )
- [ ]  Hosting Project
- [ ]  Production build
    - [ ]  Production build optimization

## Ref:

[https://madewithreactjs.com/dashboards?page=2](https://madewithreactjs.com/dashboards?page=2)

## Design :

![Untitled](Enterprise%20Dashboard%20-%20Sprih%20b5066c1499d24f3e83826046a8acc5de/Untitled.png)

Design : [https://madewithreactjs.com/mosaic-lite](https://madewithreactjs.com/mosaic-lite) 

Repo: https://github.com/cruip/tailwind-dashboard-template