import os

def check_pairs(folder_path):
    # Get all files
    files = os.listdir("/home/camila/camera/Probe_detection/images")
    
    # Separate images and xmls
    images = {f.rsplit('.', 1)[0] for f in files if f.lower().endswith(('.jpg', '.png', '.jpeg'))}
    xmls = {f.rsplit('.', 1)[0] for f in files if f.endswith('.xml')}
    
    # Find mismatches
    images_no_xml = images - xmls
    xmls_no_image = xmls - images
    
    # Print results
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
check_pairs("/home/daino/Desktop/Probe_detection/Probe_detection/images")