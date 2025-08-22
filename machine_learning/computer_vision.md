# Computer Vision


You need to create a local dependency in the network and the inputs become way less. 

Parameter sharing doesn't produce translational invariant but translational equivariant.
You want to look for the same properties of the image.

Convolution means applying different kernels/filters and it provides translational equivariant.

Reduction in parameters

FMA = Fused Multiplication and Addition

1 filter looks at 1 property

The outputs are called feature maps.
The inputs decreases in size. You cannot apply the filters again to the output otherwise there won't be anything left.

inputs have height width adn depth.
H and W are relevant only 

the bigger the stride the smaller the output we get.
What are the disadvantages? We lose information and data.
What are the advantages? continuing with smaller layers you have less competition with other neurons


Pooling: subsampling

Intuition:
Strided convolution: “Let’s learn with fewer samples — skip some data and hope the model picks up enough.”

Pooling: “Let’s summarize each patch and keep only the strongest signals.”

Regularization is something that forces the model to be simpler, this is used when the model suffers from o.overfitting. 

Dropout in CNN

if I want to connect my feature map to my multilayer I have to straighten it

In a CNN there is a feature extraction part first and then a feature classification

## Computational Graph

Deep network are hard to train because the derivatives get smaller and smaller : vanishing gradients
They are also prone to overfitting.

check Inception v1, v2 

backbone of the network = feature extraction
