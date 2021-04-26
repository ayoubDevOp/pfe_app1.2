/**
 * @param formNode {Node}
 * @param onClose {function}
 */
function Form(formNode, onClose) {
    this.formNode = formNode;
    this.tabNumber = 0;
    this.onClose = onClose;
    let formsHtml = `<div id="container" class="container">

    <div id="tab-vm" class="tab-vm"></div>
    <!-- Tab content -->

</div>  
<div class="container" style="background-color:#f1f1f1">
    <button type="button" id="closeButton" class="button1 cancelbtn">Cancel</button>
    <button type="submit"  class="button1 addbtn">Submit</button>
    <button type="button" id="addButton" class="button1 addbtn">Add</button>
</div>`;

    this.addTabVM = function () {
        this.tabNumber++;
        let tab = new TabVM(this.tabNumber).getTabVm();
        let tabLink = tab[0];
        let tabContent = tab[1];
        tabContent.forEach(value => document.getElementById("container").appendChild(value));
        tabLink.forEach(value => {
            document.getElementById("tab-vm").appendChild(value)
            value.click()
        });
    };

    this.closeForm = function () {
        for (let i = 0; i < this.formNode.childNodes.length; i++) {
            this.formNode.childNodes[i].remove();
            i--;
        }
        this.onClose();
    };

    this.createForm = function () {
        htmlToElements(formsHtml).forEach(value => this.formNode.appendChild(value));
        // setting of the add and close button
        document.getElementById("closeButton").onclick = ev => this.closeForm();
        document.getElementById("addButton").onclick = ev => this.addTabVM();
        this.addTabVM();
    };

}

