function TabVM(number) {
    this.number = number;
    this.networkNumber = 1;
    this.dockernumber = 1;

    function networkAddButton() {
        this.networkNumber++;
        let networkTab = new TabNetwork(this.number + "-" + this.networkNumber).getTabNetwork();
        let networkTabLink = networkTab[0];
        let networkTabContent = networkTab[1];
        networkTabContent.forEach(value => document.getElementById("network-container" + this.number).appendChild(value));
        networkTabLink.forEach(value => {
            document.getElementById("tab-network" + this.number).appendChild(value)
            value.click()
        });
    }

    function dockerAddButton() {
        this.dockernumber++;
        let dockerTab = new TabDocker(this.number + "-" + this.dockernumber).getTabDocker();
        let dockerTabLink = dockerTab[0];
        let dockerTabContent = dockerTab[1];
        dockerTabContent.forEach(value => document.getElementById("docker-container" + this.number).appendChild(value));
        dockerTabLink.forEach(value => {
            document.getElementById("tab-docker" + this.number).appendChild(value)
            value.click()
        });
    }

    /**
     * @return {NodeList[]}
     */
    this.getTabVm = function () {
        let tabLinkNodeList = htmlToElements(htmlTabLink(this.number));
        let tabContentNodeList = htmlToElements(htmlTabContent(this.number));
        // retrieve the add network button.
        tabContentNodeList[0].getElementsByTagName("button")[0].onclick = ev => {
            networkAddButton.call(this);
        };

        //docker
        // retrieve the add docker button.
        tabContentNodeList[0].getElementsByClassName("docker-add-button")[0].onclick = ev => {
            dockerAddButton.call(this);
        };


        return [tabLinkNodeList, tabContentNodeList];
    };


    function htmlTabLink(number) {
        return `<button type="button" class="tabLinks-vm" onclick="openTab(event, 'VM${number}','vm')">VM${number}</button>`;
    }

    function htmlTabContent(number) {
        return `<div id="VM${number}" class="tabContent-vm ">
    <label><b>Virtual Machine</b></label>
    <input type="text" placeholder="Enter Virtual Machine ID" name="vm_id${number}" required>
    <input type="text" placeholder="Enter Vagrant Box Name" name="boxName${number}" required>
    <input type="password" placeholder="Enter Password" name="password${number}" required>

    <label><b>Network</b></label>
    <button type="button" class="network-add-button">Add</button>
    <div id="network-container${number}" class="network-container">
        <div id="tab-network${number}" class="tab-network">
            <button type="button" onclick="openTab(event, 'network${number}-1','network${number}')"
                    class="tabLinks-network${number} active">
                network${number}-1
            </button>
        </div>
        <!--         newtwork Tab content -->
        <div id="network${number}-1" style="display: block;
        padding: 12px 12px;
        border: 1px solid #ccc;
        border-top: none;" class="tabContent-network${number} ">
            <select name="networkType${number}-1">
                <option value="public network">public network</option>
                <option value="privet network">privet network</option>
            </select>
            <select name="IpAssignment${number}-1">
                <option value="dhcp">dhcp</option>
                <option value="static">static</option>
            </select>
            <input type="text" placeholder="Enter the ip Address" name="ipAddress${number}-1">
        </div>
    </div>

    <div><label><b>Docker Provisioner</b></label>
        <button type="button" class="docker-add-button">Add</button>
        <div id="docker-container${number}" class="docker-container">
            <div id="tab-docker${number}" class="tab-docker">
                <button type="button" onclick="openTab(event, 'docker${number}-1','docker${number}')"
                        class="tabLinks-docker${number} active">
                    docker${number}-1
                </button>
            </div>

            <!--         docker Tab content -->
            <div id="docker${number}-1" style="display: block;
                    padding: 12px 12px;
                    border: 1px solid #ccc;
                    border-top: none;" class="tabContent-docker${number} ">
                <input type="text" placeholder="Enter Docker Image Name" name="dockerImageName${number}-1">
                <input type="text" placeholder="Enter Container Name" name="dockerContainerName${number}-1">
                <input type="text" placeholder="Enter Docker Command" name="dockerCommand${number}-1">
                <input type="text" placeholder="Enter Docker Args" name="dockerArgs${number}-1">
            </div>
        </div>
    </div>
    <label><b>Script Provisioner</b></label>
    <textarea rows="8" style="resize: none" name="scriptProvisaioner${number}">#!/bin/bash
    
    # some command
            </textarea>
    <label><b>Ansible Provisioner</b></label>
    <textarea rows="8" style="resize: none" name="ansibleProvisioning${number}"></textarea></div>`;
    }

}


