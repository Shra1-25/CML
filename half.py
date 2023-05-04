import torch
import torchvision.models as models

# Load the pretrained 32-bit ResNet50 model
model = models.resnet50(pretrained=True)

# Convert the model to half-precision floating point
model = model.half()

# Set the model to run on the GPU if available
if torch.cuda.is_available():
    model.cuda()

# Define a sample input tensor to test the model
input_tensor = torch.randn(1, 3, 224, 224).half()

# Run a forward pass of the model on the input tensor
output = model(input_tensor)
import pdb; pdb.set_trace()
# Save the converted model to a file
torch.save(model.state_dict(), "resnet50_16bit.pth")
