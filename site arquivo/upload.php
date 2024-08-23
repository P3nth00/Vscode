<?php
// Verifica se o formulário foi enviado
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Verifica se há um arquivo enviado
    if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
        $uploadDir = 'uploads/'; // Diretório onde os arquivos serão armazenados
        $uploadFile = $uploadDir . basename($_FILES['file']['name']); // Caminho completo do arquivo

        // Move o arquivo para o diretório de uploads
        if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadFile)) {
            echo "Arquivo enviado com sucesso!"; // Mensagem de sucesso
        } else {
            echo "Ocorreu um erro ao enviar o arquivo."; // Mensagem de erro
        }
    } else {
        echo "Nenhum arquivo enviado ou erro no upload."; // Mensagem de erro
    }
}
?>
