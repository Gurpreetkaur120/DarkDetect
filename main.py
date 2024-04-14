from pathlib import Path
import sys
import gemini
import tamper
import cv2

def main(image_path):
    # Analyze image for deceptive/manipulative content
    try:
        analysis_result = gemini.analyze_image(image_path)
        print("Analysis Result:")
        print(analysis_result)
    except FileNotFoundError as e:
        print(e)

    # Detect tampering in the image
    print("\nDetecting Tampering:")
    is_tampered, mask = tamper.detect_tampering(image_path)
    if is_tampered:
        print("The image has been tampered with.")
    else:
        print("The image has not been tampered with.")

    # Display the binary mask for visualization
    cv2.imshow("Mask", mask)
    cv2.waitKey(5000)  # Wait for 5 seconds (5000 milliseconds)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    main(image_path)