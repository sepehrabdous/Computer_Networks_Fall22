# Assignment 4: Internet Measurement

## Due Date: Friday, December 9, 2021 at 5 pm EST

In this assignment, you will analyze publicly-available measurement data to understand important properties of the Internet.

## Submission Instructions

For the assignment, submit (via [Gradescope](https://www.gradescope.com/)) (i) the answers to the questions below as well as a "readme" section, in PDF format and (ii) the code for scripts you wrote to analyze the data. Name the pdf [JHED]_analysis.pdf and zip your code up as [JHED]_code.

All answers to the questions asked should be written in full and clear sentences.

## Readme (10 points)

There should be a section in the PDF, briefly describing your code and instructions on how to run it (a README basically). You should also mention what platform you used to run your code on. Place this either at the beginning or the end of your PDF.

## Code

You can use any language you prefer for this assignment. Your code should be able to be run and should match the output found in your answers. Not matching these conditions gives you no credit for the assignment.

## Router Measurement (55 points)

Many networks collect Netflow measurements directly from the routers. For more information, read the [Wikipedia](http://en.wikipedia.org/wiki/Netflow) and [Cisco](http://www.cisco.com/en/US/products/ps6601/products_ios_protocol_group_home.html). In this part of the assignment, you'll analyze a five-minute trace of Netflow records captured from a router in the [Internet2](http://www.internet2.edu/) backbone that connects the major research universities in the United States. The records have been parsed into CSV (comma-separated variable) format, with the names of the fields listed in the first row of the file. Internet2 collects Netflow measurements with 1/100 packet sampling, so the data reflects 1% of the traffic at the router.

The important fields in the Netflow data are: `Packets` and `Bytes` (the number of packets and bytes in the flow, respectively), `Date first seen`, `Time first seen (m:s)`, `Date last seen` and `Time last seen (m:s)` (the timestamps of the first and last packets in the flow, respectively), `Src IP addr` and `Dst IP addr` (the source and destination IP addresses, respectively), `Src port` and `Dst port` (the source and destination transport port numbers, respectively), `Protocol` (the transport protocol, e.g., TCP, UDP). For example, looking at the first two lines of `./data/netflow.csv`:

|Date first seen|Time first seen (m:s)|Date last seen|Time last seen (m:s)|Duration (s)|Protocol|Src IP addr|Src port|Dst IP addr|Dst port|Packets|Bytes|Flags|Input interface|Output interface|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|10/29/15|04:48.9|10/29/15|04:48.9|0|TCP|116.211.0.90|52704|128.112.186.67|9095|1|40|....S.|120|70|

you have a flow with one 40-byte packet that arrived at the time 04:48.9. The packet was sent by source address 116.211.0.90 to the destination address 128.112.186.67. The source port is 52704 (an [ephemeral port](https://en.wikipedia.org/wiki/Ephemeral_port)) and the destination port is 9095. The protocol this flow is using to transmit data is TCP.

### Question 1.1 (20 points: 5 points for each of the 3 graphs, 5 points for discussion)

Researchers often summarize a large collection of measurement data using distribution functions. Imagine you have a list of Web pages with different sizes, in terms of number of bytes. The cumulative distribution function (CDF) of page sizes would have a y-axis of "the fraction of Web pages that are less than or equal to x bytes", and an x-axis of the number of bytes. The graph would start at y=0, since no Web pages have less than or equal to 0 bytes, and reach y=1 when x reaches the size of the largest page.

Create a CDF where the x-axis is the number of bytes in a flow, and the y-axis is the percentage of flows with that many bytes or less. Make this same plot but for flows transported by UDP and TCP. Provide two observations about trends or patterns you can determine from this graph. Make sure to use logarithmic scales for x-axis and linear scale for y-axis for figures to be clear.

### Question 1.2 (10 points: 2.5 points for each top ten list, 2.5 points for the percentages)

Get the number of flows for each source IP address, only considering its 16-bit prefix (for example: the IP addresses 255.255.0.1 and 255.255.0.2 are counted as there being two 255.255 addresses). What are the top ten IP address prefixes, and what percentage of all the flows recorded are they involved in? (No need to report the percentage per source IP address, just report the aggreagate percentage for top ten source IP addresses.)

Now, aggregate the number of bytes by source IP addresses the same way. What are the top ten IP address prefixes in this case, and what percentage of bytes sent across all flows are they responsible for (no need to report the percentage per source IP address, just report the aggreagate percentage for top ten source IP addresses)?

### Question 1.3 (5 points: 2 points for describing port number correctly, 3 points for correct percentage)

The src/dst port number of a connection corresponds to the src/dst port number for a UDP/TCP packet. This number represents the application protocol that the packet either came from or is sent to. See [this wikipedia page](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) for more information on what these port numbers mean.

Pick a port number less than 1024, provide the type of service it's associated with, and report the percentage of flows it appears in as the src port and the percentage of flows it appears in as the dst port.

### Question 1.4 (10 points: 2 points for each of the 3 percentages, 4 points for discussion)

Observe that this router is responsible for the address block 128.112.0.0/16. What percentage of bytes is sent from this router, and what percentage is sent to this router? What percentage of bytes have a destination and source IP address that are both in this address block? What do these metrics tell you about traffic happening with this router?

### Question 1.5 (10 points)

The data you worked with comes from a university's campus, from 6:05 AM to 6:10 AM. What changes would expect in your answers for the previous questions if this data was collected from a router that was serving devices at a busy public cafe during the afternoon? Provide reasons as to why.

## BGP Measurement (45 points)

BGP routing changes disrupt the delivery of data traffic and consume bandwidth and CPU resources on the routers. In this part of the assignment, you will analyze BGP update messages logged by [RouteViews](http://www.routeviews.org/) to analyze BGP (in)stability and convergence behavior. RouteViews has BGP sessions with a variety of different ISPs, and logs the update messages sent on each of these sessions. The data for the homework has already been parsed and provided for you, but to see more sessions, go to the RouteViews [archive](ftp://archive.routeviews.org/) and pick one of the directories starting with "route-views" (e.g., "route-views.eqix"), and find update data from a particular month, e.g., [this directory](ftp://archive.routeviews.org/route-views.eqix/bgpdata/2010.08/UPDATES/) has files logging the BGP updates for each 15-minute interval, and [this directory](ftp://archive.routeviews.org/route-views.eqix/bgpdata/2010.08/RIBS/) has the periodic routing-table (Routing Information Base) dumps. These files are in a compressed, binary format (e.g., gzip or bzip2). You will need [tools](http://www.routeviews.org/tools.html) to "uncompress" and parse the data. In particular, the bgpdump tool is probably the best choice for parsing the update messages.


BGP is an incremental protocol, sending an update message only when the route for a destination prefix changes. So, most analysis of BGP updates must start with a snapshot of the RIB, to know the initial route for each destination prefix. You will use the RIB snapshot `./data/bgp_route.csv` to identify the initial set of destination prefixes, and then analyze the 15 minutes of updates before this snapshot, `./data/bgp_update.csv`.

The important fields for the snapshot are: `TIME` which is when it was recorded, `NEXT_HOP` is the IP address of the border router to send packets for the destinations of this entry, `FROM` is border router's ip address and AS this entry comes from, `ASPATH` is the path through ASes it takes to reach the destination , and `PREFIX` is the IP addresses that refer to this route. For example, looking at the first two lines of `./data/bgp_route.csv`:

|TIME|NEXT_HOP|FROM|ASPATH|PREFIX|ORIGIN|
|---|---|---|---|---|---|
|03/28/21 04:00:00|85.114.0.217|194.153.0.253 AS5413|286 3257 13335|1.0.0.0/24|IGP|

this entry was recorded on March 28th, 2021 at 4AM. It comes from the router at IP address 194.153.0.25, which is from the AS 5413. The path of ASES is 286, 3257 and 13335. This path is taken by packets destined for addresses 1.0.0.0/24.

The important fields for the snapshot include the ones mentioned for the BGP snapshots, but also includes
`COMMAND` which is the type of message sent from the AS followed by the IP addresses affected. As well `ASPATH` now refers to the path related by the message's type. For example, looking at the first two lines of `./data/bgp_update.csv`:

|TIME|FROM|ASPATH|NEXT_HOP|COMMAND|ORIGIN|
|---|---|---|---|---|---|
|45:00.3|208.51.134.246 AS3549|3549 3356 8820 8820 8820 8820|208.51.134.246|ANNOUNCE 46.41.11.0/24|IGP|

this entry was recorded 45 minutes and 3 microseconds into the hour. It comes from the router at IP address 208.51.134.246, which is from the AS 3549. The path of ASes here is 3549, 3356, and 8820. It is advertising this path for reaching ip addresses 46.41.11.0/24.

### Question 2.1 (15 points: 5 points for top ten list, 5 points for percentage, 5 for points for discussion)

From the `bgp_route.csv`, what are the 10 most frequent ASes in all the BGP paths? What percentage of paths are they found in? Using your favorite browser and search engine, give the name of the AS and the country they belong to (Hint: search for "AS number lookup", give the country's full name). Why might it be problematic for an AS to be commonly found in these routes?

### Question 2.2 (10 points: 5 points for graph, 5 points for discussion)

Plot a cumulative distribution function (CDF) where the x-axis is the length of a BGP path and y-axis is the proportion of the paths with that length or less. The length is the number of **unique** ASes in an entry's `ASPATH`. What does this graph tell you about BGP route lengths? What does this graph tell you about a packet’s travel across the internet?

### Question 2.3 (10 points: 5 points for graph, 5 points for average)

Using `bgp_updates.csv`, how many BGP updates are done per minute, on average? Make a graph where the x-axis is time and the y-axis is the number of updates at that second.

### Question 2.4 (10 points: 5 points for graph, 5 points for discussion)

Plot a CDF where the x-axis is the top percentage of ASes by the number of updates and the y-axis is the percentage of updates messages that are from that top percentage. Include all ASes from `bgp_route.csv`, not just the `bgp_update.csv`. Make sure to use logarithmic scales for graph axes if the distribution is not clear. What can you infer about the ASes tracked here, specifically about their stability?
