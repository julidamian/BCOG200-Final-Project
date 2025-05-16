#following test from wolfpack demo
import pytest
from PIL import Image
from final_project import ImageProcessor
import os

def create_test_image(size=(100, 100), color=255):
  """Monochromatic canvas for testing"""
  return Image.new("L", size, color)

def test_outline_image_return_image():
  processor = ImageProcessor()
  test_image = create_test_image()
  outline = processor.outline_image(test_image)

  assert isinstance(outline, Image.Image), "should get PIL Image"
  assert outlined.size == test_image.size, "Outline image size mismatch"

def test_load_image(tmp_path):
  processor = ImageProcessor()

  image = create_test_image()
  temp_path = tmp_path / "test_image.jpg"
  image.save(temp_path)


  processed = processor.load_image(str(temp_path), max_size=(50, 50))

  assert isinstance(processed, Image.Image)
  assert processor.original_image.size[0] <= 50
  assert processor.original_image.mode == "L"
  
