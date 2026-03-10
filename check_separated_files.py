
import os

def check_pairs(images_folder, labels_folder):
    # Get files from respective folders
    image_files = os.listdir(images_folder)
    label_files = os.listdir(labels_folder)
    
    # Separate images and xmls
    images = {f.rsplit('.', 1)[0] for f in image_files 
              if f.lower().endswith(('.jpg', '.png', '.jpeg'))}
    
    xmls = {f.rsplit('.', 1)[0] for f in label_files 
            if f.lower().endswith('.xml')}
    
    # Find mismatches
    images_no_xml = images - xmls
    xmls_no_image = xmls - images
    
    # Print results (unchanged)
    if images_no_xml:
        print("Images without XML:")
        for name in sorted(images_no_xml):
            print(f"  {name}")
    
    if xmls_no_image:
        print("\nXMLs without image:")
        for name in sorted(xmls_no_image):
            print(f"  {name}")
    
    if not images_no_xml and not xmls_no_image:
        print("✓ All paired correctly!")

# Usage
check_pairs(
    "/home/camila/camera/Probe_detection/images",
    "/home/camila/camera/Probe_detection/labels"
)
