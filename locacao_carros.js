const readline = require('readline');

// Configuração do readline para interação com o usuário
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Array para armazenar os veículos
let veiculos = [];

// Função para adicionar um veículo
function adicionarVeiculo() {
    rl.question("Digite a marca do veículo: ", (marca) => {
        rl.question("Digite o modelo do veículo: ", (modelo) => {
            rl.question("Digite o ano do veículo: ", (ano) => {
                rl.question("Digite o status do veículo (Disponível/Indisponível): ", (status) => {
                    rl.question("Digite o valor da diária do veículo: ", (diaria) => {
                        // Criando o objeto do veículo
                        const veiculo = {
                            marca: marca,
                            modelo: modelo,
                            ano: parseInt(ano),
                            status: status,
                            diaria: parseFloat(diaria)
                        };

                        // Adicionando o veículo ao array
                        veiculos.push(veiculo);
                        console.log("Veículo adicionado com sucesso!\n");
                        menu(); // Volta ao menu após adicionar
                    });
                });
            });
        });
    });
}

// Função para listar os veículos
function listarVeiculos() {
    if (veiculos.length === 0) {
        console.log("Nenhum veículo cadastrado.\n");
    } else {
        console.log("Lista de Veículos:");
        veiculos.forEach((veiculo, index) => {
            console.log(`Veículo ${index + 1}:`);
            console.log(`  Marca: ${veiculo.marca}`);
            console.log(`  Modelo: ${veiculo.modelo}`);
            console.log(`  Ano: ${veiculo.ano}`);
            console.log(`  Status: ${veiculo.status}`);
            console.log(`  Diária: R$ ${veiculo.diaria.toFixed(2)}`);
            console.log('-------------------------');
        });
    }
    menu(); // Volta ao menu após listar
}

// Menu interativo
function menu() {
    rl.question(
        "Escolha uma opção:\n" +
        "1. Adicionar veículo\n" +
        "2. Listar veículos\n" +
        "3. Sair\n" +
        "Digite o número da opção: ",
        (opcao) => {
            switch (opcao) {
                case "1":
                    adicionarVeiculo();
                    break;
                case "2":
                    listarVeiculos();
                    break;
                case "3":
                    console.log("Saindo do sistema...");
                    rl.close(); // Fecha o readline e encerra o programa
                    break;
                default:
                    console.log("Opção inválida. Tente novamente.\n");
                    menu(); // Volta ao menu em caso de opção inválida
            }
        }
    );
}

// Iniciar o sistema
menu();

