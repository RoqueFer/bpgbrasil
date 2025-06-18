// ARQUIVO: js/dropdown.js

document.addEventListener('DOMContentLoaded', () => {
    // Seleciona todos os botões que devem acionar um dropdown
    const dropdownToggles = document.querySelectorAll('[data-dropdown-toggle]');

    dropdownToggles.forEach(toggleButton => {
        toggleButton.addEventListener('click', (event) => {
            event.stopPropagation(); // Impede que o clique se propague para o document

            const targetDropdownId = toggleButton.dataset.dropdownToggle;
            const targetDropdown = document.getElementById(targetDropdownId);

            // Fecha todos os outros dropdowns abertos (e remove a classe 'active' dos botões)
            document.querySelectorAll('.dropdown-menu.show').forEach(openDropdown => {
                if (openDropdown !== targetDropdown) {
                    openDropdown.classList.remove('show');
                    document.querySelector(`[data-dropdown-toggle="${openDropdown.id}"]`).classList.remove('active');
                }
            });

            // Alterna a visibilidade do dropdown alvo e a classe 'active' do botão
            targetDropdown.classList.toggle('show');
            toggleButton.classList.toggle('active');
        });
    });

    // Fecha os dropdowns se o usuário clicar fora deles
    document.addEventListener('click', (event) => {
        document.querySelectorAll('.dropdown-menu.show').forEach(openDropdown => {
            openDropdown.classList.remove('show');
            // Remove a classe 'active' de todos os botões que estavam abertos
            document.querySelector(`[data-dropdown-toggle="${openDropdown.id}"]`).classList.remove('active');
        });
    });

    // Impede que o clique dentro do dropdown-menu feche-o
    document.querySelectorAll('.dropdown-menu').forEach(menu => {
        menu.addEventListener('click', (event) => {
            event.stopPropagation();
        });
    });
});