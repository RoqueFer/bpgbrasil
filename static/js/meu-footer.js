// ARQUIVO: js/meu-footer.js

class MeuFooter extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <footer class="site-footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h3>Sobre Nós</h3>
                        <p>
                            O Boletim Paranaense de Geociências é um periódico científico fundado na década de 1950, dedicado a publicar artigos sobre geologia do Brasil e de toda a América do Sul.
                        </p>
                    </div>
                    <div class="footer-section">
                        <h3>Contato</h3>
                        <ul class="contact-list">
                            <li><i class="fa fa-envelope"></i> Email: bpg.ufpr@gmail.com</li>
                            <li><i class="fa fa-building"></i> Universidade Federal do Paraná</li>
                        </ul>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>&copy; 2025 Casa de Júniors. Todos os direitos reservados.</p>
                    <div class="social-links">
                        <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                        <a href="#" aria-label="Twitter"><i class="fab fa-x-twitter"></i></a>
                        <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
            </div>
        </footer>
        `;
    }
}

customElements.define('meu-footer', MeuFooter);