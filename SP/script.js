/* Função para buscar e mostrar produtos no DOM */
function fetchProducts() {
    fetch('list_products.php')
    .then(response => response.json()) // Converter a resposta para JSON
    .then(data => {
        const productList = document.getElementById('productList');
        productList.innerHTML = ''; // Limpar a lista

        // Loop por cada produto e adicionar ao DOM
        data.forEach(product => {
            const div = document.createElement('div');
            div.innerHTML = `
                <h3>${product.nome}</h3>
                <p>Preço: ${product.price}</p>
                <p>${product.description}</p>
                <button onclick="deleteProduct(${product.id})">Excluir</button>
                <button onclick="editProduct(${product.id}, '${product.nome}',
                ${product.price}, '${product.description}')">Editar</button>
            `;
            productList.appendChild(div);
        });
    });
}

// Função para excluir produto
function deleteProduct(id) {
    if (confirm('Tem certeza que deseja excluir este produto?')) {
        fetch(`delete_product.php?id=${id}`, { method: 'GET' }) // Fazer requisição GET para deletar
        .then(() => fetchProducts()); // Atualizar a lista de produtos
    }
}

// Função para editar produto
function editProduct(id, name, price, description) {
    document.getElementById('name').value = name;
    document.getElementById('price').value = price;
    document.getElementById('description').value = description;

    const form = document.getElementById('productForm');
    form.action = `edit_product.php?id=${id}`; // Mudar o destino do formulário para o script de edição
}

// Chamar a função para mostrar produtos ao carregar a página
window.onload = fetchProducts;