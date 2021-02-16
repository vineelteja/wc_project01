import os
arr = os.listdir("/Users/darkpirate/Downloads/docker_volume/node/westcliff_801/project1/images/rollercoaster/")
for each in arr:
    print(f'''
            <a
            class="grid-item"
            href="images/rollercoaster/{each}"
            data-lightbox="gallery-item"
            title="18 and Stewie | abs0006"
            >
            <img
                src="images/rollercoaster/{each}"
                alt="18 and Stewie | abs0006"
            />
            </a>
    
    ''')