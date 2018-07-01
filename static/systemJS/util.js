function parseXML(xmlFile){
    // 创建解析XML后的DOM对象
    let xmlDoc = null;
    // 根据不同浏览器进行解析
    if(window.DOMParser){
        // 其他浏览器
        let parser = new DOMParser();
        xmlDoc = parser.parseFromString(xmlFile,"application/xml");
    }else{
        // IE浏览器
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async = false;
        xmlDoc.loadXML(xmlFile);
    }
    return xmlDoc;
}
