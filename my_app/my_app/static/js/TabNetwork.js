function TabNetwork(number) {
    this.number = number;

    /**
     * @return {NodeList[]}
     */
    this.getTabNetwork = function () {
        return [htmlToElements(htmlTabLinkNetwork(this.number)), htmlToElements(htmlTabContentNetwork(this.number))];
    };

// todo change tablinks to tabLinks.
    function htmlTabLinkNetwork(number) {
        return `<button type="button" onclick="openTab(event, 'network${number}','network${number.substr(0, number.indexOf('-'))}')" class="tabLinks-network${number.substr(0, number.indexOf('-'))}">network${number}</button>`;
    }

    function htmlTabContentNetwork(number) {
        return `<div id="network${number}" style="display: none;
    padding: 12px 12px;
    border: 1px solid #ccc;
    border-top: none;" class="tabContent-network${number.substr(0, number.indexOf('-'))}">
    <select name="networkType${number}">
        <option value="public network">public network</option>
        <option value="privet network">privet network</option>
    </select>
    <select name="IpAssignment${number}">
        <option value="dhcp">dhcp</option>
        <option value="static">static</option>
    </select>
    <input type="text" placeholder="Enter the ip Address" name="ipAddress${number}"  > 
</div>`;
    }

}


