import os
import gdown

# URL файла или его идентификатор
url = "https://drive.google.com/uc?id=1z08IQnnQE8LcQKmrtfycvfvNVqHyjmy7"
# Путь, куда будет сохранён файл
output_dir = "./models/DuckingModel/weights"
output_file = os.path.join(output_dir, "model.h5")

# Проверяем, существует ли директория, если нет - создаём
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Скачивание файла
gdown.download(url, output_file, quiet=False)
