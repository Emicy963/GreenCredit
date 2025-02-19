document.addEventListener('DOMContentLoaded', function() {
    const addButton = document.getElementById('add-item');
    const container = document.getElementById('items-container');
    let formCount = document.querySelectorAll('.item-form').length;

    addButton.addEventListener('click', function() {
        const newForm = container.children[0].cloneNode(true);
        const newHtml = newForm.innerHTML.replace(/__prefix__/g, formCount);
        const newDiv = document.createElement('div');
        newDiv.className = 'item-form';
        newDiv.innerHTML = newHtml;
        container.appendChild(newDiv);
        
        const totalForms = document.getElementById('id_form-TOTAL_FORMS');
        totalForms.value = ++formCount;
    });
});