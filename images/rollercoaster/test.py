import os
img_folder = "airplans"
arr = os.listdir(f"/Users/darkpirate/Downloads/docker_volume/node/westcliff_801/project1/images/airplans/")
for each in arr:
    print(f'''
            <a
            class="grid-item"
            href="images/{img_folder}/{each}"
            data-lightbox="gallery-item"
            title="18 and Stewie | abs0006"
            >
            <img
                src="images/{img_folder}/{each}"
                alt="18 and Stewie | abs0006"
            />
            </a>
    
    ''')