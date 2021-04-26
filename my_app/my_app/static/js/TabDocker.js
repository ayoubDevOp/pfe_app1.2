function TabDocker(number) {
    this.number = number;

    /**
     * @return {NodeList[]}
     */
    this.getTabDocker = function () {
        return [htmlToElements(htmlTabLinkDocker(this.number)), htmlToElements(htmlTabContentDocker(this.number))];
    };

    function htmlTabLinkDocker(number) {
        return `<button type="button" onClick="openTab(event, 'docker${number}','docker${number.substr(0, number.indexOf('-'))}')" class="tabLinks-docker${number.substr(0, number.indexOf('-'))}">docker${number}</button>`;
    }

    function htmlTabContentDocker(number) {
        return `<div id="docker${number}" style="display: none;
                    padding: 12px 12px;
                    border: 1px solid #ccc;
                    border-top: none;" class="tabContent-docker${number.substr(0, number.indexOf('-'))} ">
                    <input type="text" placeholder="Enter Docker Image Name" name="dockerImageName${number}">  
                    <input type="text" placeholder="Enter Container Name" name="dockerContainerName${number}">  
                    <input type="text" placeholder="Enter Docker Command" name="dockerCommand${number}">  
                    <input type="text" placeholder="Enter Docker Args" name="dockerArgs${number}">  
                </div>`;
    }
}


