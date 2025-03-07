document.getElementById('generate-btn').addEventListener('click', function () {
    const imageUpload = document.getElementById('image-upload');
    const captionInput = document.getElementById('caption-input').value;

    if (!imageUpload.files[0]) {
        alert('Por favor, selecione uma imagem.');
        return;
    }

    const reader = new FileReader();
    reader.onload = function (e) {
        const img = new Image();
        img.src = e.target.result;

        img.onload = function () {
            const sticker = document.createElement('div');
            sticker.className = 'sticker';

            const imgElement = document.createElement('img');
            imgElement.src = img.src;
            sticker.appendChild(imgElement);

            if (captionInput.trim() !== '') {
                const caption = document.createElement('div');
                caption.className = 'caption';
                caption.textContent = captionInput;
                sticker.appendChild(caption);
            }

            const output = document.getElementById('sticker-output');
            output.innerHTML = '';
            output.appendChild(sticker);

            // Converter a figurinha em imagem usando html2canvas
            html2canvas(sticker).then(canvas => {
                const img = document.createElement('img');
                img.src = canvas.toDataURL('image/png'); // Converte o canvas para uma imagem PNG
                output.innerHTML = ''; // Limpa o conteúdo anterior
                output.appendChild(img); // Exibe a imagem gerada

                // Adiciona um botão para compartilhar no WhatsApp
                const whatsappBtn = document.createElement('button');
                whatsappBtn.textContent = 'Enviar por WhatsApp';
                whatsappBtn.id = 'whatsapp-btn';
                output.appendChild(whatsappBtn);

                // Adiciona o evento de clique no botão do WhatsApp
                whatsappBtn.addEventListener('click', () => {
                    sendToWhatsApp(img.src);
                });
            });
        };
    };
    reader.readAsDataURL(imageUpload.files[0]);
});

function sendToWhatsApp(imageSrc) {
    // Cria um link temporário para a imagem
    const link = document.createElement('a');
    link.href = imageSrc;
    link.download = 'figurinha.png'; // Nome do arquivo para download
    document.body.appendChild(link);
    link.click(); // Inicia o download da imagem
    document.body.removeChild(link);

    // Abre o WhatsApp Web em uma nova aba
    const whatsappUrl = `https://web.whatsapp.com`;
    window.open(whatsappUrl, '_blank');
}