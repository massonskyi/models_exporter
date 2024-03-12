import os
__all__ = ['rename_images']
def rename_images(directory_path):
    with open("./dataset.txt", "w") as f:
        for i, filename in enumerate(os.listdir(directory_path), start=1):
            # Формируем новое имя файла
            new_filename = f"drone_frame_{i}.jpg"

            # Формируем полные пути к старому и новому файлу
            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_filename)

            # Переименовываем файл
            os.rename(old_file_path, new_file_path)
            f.write(f"{new_file_path}\n")
            print(f"Renamed file: {old_file_path} -> {new_file_path}")

# rename_images("./dataset/images/")