import argparse
import subprocess

parser = argparse.ArgumentParser(description="yolov4-tiny inference")
parser.add_argument("path", metavar="PATH", type=str, help="Path to image")

if __name__ == "__main__":
    args = parser.parse_args()
    image_path = args.path
    command = "./darknet detector test data/obj.data cfg/yolov4-tiny-obj.cfg cfg/yolov4-tiny-obj_best.weights".split(' ')
    command.append(image_path)
    subprocess.run(command)
