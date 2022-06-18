#version 330 core

in vec3 newColor;
in vec2 outTexCoord;

out vec4 outColor;
uniform sampler2D texSampler;

void main()
{

    outColor = texture(texSampler,outTexCoord);
}
