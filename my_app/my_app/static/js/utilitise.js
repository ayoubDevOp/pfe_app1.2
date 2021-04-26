/**
 * @param {String} HTML representing any number of sibling elements
 * @return {NodeList}
 */
function htmlToElements(html) {
    let template = document.createElement('template');
    template.innerHTML = html;
    return template.content.childNodes;
}

function openTab(evt, TabName, type) {

    let i, tabContent, tabLinks;
    tabContent = document.getElementsByClassName("tabContent" + "-" + type);
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }
    tabLinks = document.getElementsByClassName("tabLinks" + "-" + type);
    for (i = 0; i < tabLinks.length; i++) {
        tabLinks[i].className = tabLinks[i].className.replace(" active", "");
        // tabLinks[i].className = tabLinks[i].className.replace(" active-" + type, "");
    }
    document.getElementById(TabName).style.display = "block";
    evt.currentTarget.className += " active";
}