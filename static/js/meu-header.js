// ARQUIVO: js/meu-header.js

class MeuHeader extends HTMLElement {
    connectedCallback() {
        // O caminho para a logo agora precisa pensar a partir da raiz do site
        const logoPath = './Logos - Parceiros/LOGO ATUALIZADA SENHOR AMADO.png';

        this.innerHTML = `
        {% load static %}
<div class="container_madeira">
  <img src="{% static 'Logos - Parceiros/logo_final_final_3_final_definitivo_endgame.png' %}" alt="Logo BPG Braisl" class="logo">
  <h1 class="header_font">Boletim Paranaense de Geociências</h1>
</div>
<div class="container_cinza">
  <div class="container_menu">
    {# Substitua 'nome_da_url' pelos nomes definidos no seu arquivo urls.py #}
    <a href="{% url 'artigos' %}">Artigos</a>
    <p class="divisor">|</p>
    <a href="{% url 'envie_seu_artigo' %}">Envie seu Artigo</a>
    <p class="divisor">|</p>
    <a href="{% url 'normas' %}">Normas</a>
    <p class="divisor">|</p>
    <a href="{% url 'consultivo' %}">Consultivo</a>
    <p class="divisor">|</p>
    <a href="{% url 'fale_conosco' %}">Fale Conosco</a>
  </div>
</div>
        `;
    }
}

customElements.define('meu-header', MeuHeader);