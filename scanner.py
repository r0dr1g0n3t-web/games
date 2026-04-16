import os
import json

def generate_database():
    games = []
    # Scans for directories starting with 'g' (g01, g02...)
    folders = [f for f in os.listdir('.') if os.path.isdir(f) and f.startswith('g')]
    
    for folder in sorted(folders):
        json_path = os.path.join(folder, 'game.json')
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Add automatic pathing for the catalog
                data['id'] = folder
                data['path'] = f"./{folder}/index.html"
                data['icon'] = f"./{folder}/icon.png"
                games.append(data)
    
    with open('database.json', 'w', encoding='utf-8') as f:
        json.dump(games, f, indent=2, ensure_ascii=False)
    print(f"Successfully indexed {len(games)} games.")

if __name__ == "__main__":
    generate_database()