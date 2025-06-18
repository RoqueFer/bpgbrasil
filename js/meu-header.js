// ARQUIVO: js/meu-header.js

class MeuHeader extends HTMLElement {
    connectedCallback() {
        // O caminho para a logo agora precisa pensar a partir da raiz do site
        const logoPath = '/Logos - Parceiros/logo_pronta.png';

        this.innerHTML = `
        <header>
            <div class="container_madeira">
                <a href="main.html" class="logo-link">
                    <img src="${logoPath}" alt="Logo BPG Brasil - Ir para a página principal" class="logo">
                </a>
                <h1 class="header_font">Boletim Paranaense de Geociências</h1>
            </div>
            <div class="container_cinza">
                <div class="container_menu">
                    <a href="procurePor.html">Artigos</a>
                    <p class="divisor">|</p>
                    <a href="envie_seu_artigo.html">Envie seu Artigo</a>
                    <p class="divisor">|</p>
                    <a href="normas.html">Normas</a>
                    <p class="divisor">|</p>
                    <a href="fale_conosco.html">Consultivo</a>
                    <p class="divisor">|</p>
                    <a href="fale_conosco.html">Fale Conosco</a>
                </div>
            </div>
        </header>
        `;
    }
}

customElements.define('meu-header', MeuHeader);