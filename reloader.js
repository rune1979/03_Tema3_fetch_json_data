function reloadGraph() {
   var now = new Date();

   document.images['graph'].src = 'foo.png?' + now.getTime();
   //document.text/plain['graph'].data = 'tekst.txt?' + now.getTime();
   //$('#refresh').load(location.href + ' #tekst');

   // Start new timer (1 min)
   timeoutID = setTimeout('reloadGraph()', 5000);
}

