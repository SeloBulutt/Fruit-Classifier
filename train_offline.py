from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
model = YOLO('yolov8n.pt')


def main():
    model.train(data='Dataset/SplitData/data.yaml', epochs=30, patience=500)


if __name__ == '__main__':
    main()