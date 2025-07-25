add configs for image generation to config.yaml and add to the nec methods in main. Be extensive for actual options on video generation, but no need to include things like http options.

Add tests as nec.

Revelvant documentation below:

pydantic model genai.types.GenerateImagesConfig
Bases: BaseModel

The config for generating an images.

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

Show JSON schema
{
   "title": "GenerateImagesConfig",
   "description": "The config for generating an images.",
   "type": "object",
   "properties": {
      "httpOptions": {
         "anyOf": [
            {
               "$ref": "#/$defs/HttpOptions"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Used to override HTTP request options."
      },
      "outputGcsUri": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Cloud Storage URI used to store the generated images.\n      ",
         "title": "Outputgcsuri"
      },
      "negativePrompt": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Description of what to discourage in the generated images.\n      ",
         "title": "Negativeprompt"
      },
      "numberOfImages": {
         "anyOf": [
            {
               "type": "integer"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Number of images to generate.\n      ",
         "title": "Numberofimages"
      },
      "aspectRatio": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Aspect ratio of the generated images. Supported values are\n      \"1:1\", \"3:4\", \"4:3\", \"9:16\", and \"16:9\".\n      ",
         "title": "Aspectratio"
      },
      "guidanceScale": {
         "anyOf": [
            {
               "type": "number"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Controls how much the model adheres to the text prompt. Large\n      values increase output and prompt alignment, but may compromise image\n      quality.\n      ",
         "title": "Guidancescale"
      },
      "seed": {
         "anyOf": [
            {
               "type": "integer"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Random seed for image generation. This is not available when\n      ``add_watermark`` is set to true.\n      ",
         "title": "Seed"
      },
      "safetyFilterLevel": {
         "anyOf": [
            {
               "$ref": "#/$defs/SafetyFilterLevel"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Filter level for safety filtering.\n      "
      },
      "personGeneration": {
         "anyOf": [
            {
               "$ref": "#/$defs/PersonGeneration"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Allows generation of people by the model.\n      "
      },
      "includeSafetyAttributes": {
         "anyOf": [
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Whether to report the safety scores of each generated image and\n      the positive prompt in the response.\n      ",
         "title": "Includesafetyattributes"
      },
      "includeRaiReason": {
         "anyOf": [
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Whether to include the Responsible AI filter reason if the image\n      is filtered out of the response.\n      ",
         "title": "Includeraireason"
      },
      "language": {
         "anyOf": [
            {
               "$ref": "#/$defs/ImagePromptLanguage"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Language of the text in the prompt.\n      "
      },
      "outputMimeType": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "MIME type of the generated image.\n      ",
         "title": "Outputmimetype"
      },
      "outputCompressionQuality": {
         "anyOf": [
            {
               "type": "integer"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Compression quality of the generated image (for ``image/jpeg``\n      only).\n      ",
         "title": "Outputcompressionquality"
      },
      "addWatermark": {
         "anyOf": [
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Whether to add a watermark to the generated images.\n      ",
         "title": "Addwatermark"
      },
      "imageSize": {
         "anyOf": [
            {
               "type": "string"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "The size of the largest dimension of the generated image.\n      Supported sizes are 1K and 2K (not supported for Imagen 3 models).\n      ",
         "title": "Imagesize"
      },
      "enhancePrompt": {
         "anyOf": [
            {
               "type": "boolean"
            },
            {
               "type": "null"
            }
         ],
         "default": null,
         "description": "Whether to use the prompt rewriting logic.\n      ",
         "title": "Enhanceprompt"
      }
   },
   "$defs": {
      "HttpOptions": {
         "additionalProperties": false,
         "description": "HTTP options to be used in each of the requests.",
         "properties": {
            "baseUrl": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "The base URL for the AI platform service endpoint.",
               "title": "Baseurl"
            },
            "apiVersion": {
               "anyOf": [
                  {
                     "type": "string"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Specifies the version of the API to use.",
               "title": "Apiversion"
            },
            "headers": {
               "anyOf": [
                  {
                     "additionalProperties": {
                        "type": "string"
                     },
                     "type": "object"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Additional HTTP headers to be sent with the request.",
               "title": "Headers"
            },
            "timeout": {
               "anyOf": [
                  {
                     "type": "integer"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Timeout for the request in milliseconds.",
               "title": "Timeout"
            },
            "clientArgs": {
               "anyOf": [
                  {
                     "additionalProperties": true,
                     "type": "object"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Args passed to the HTTP client.",
               "title": "Clientargs"
            },
            "asyncClientArgs": {
               "anyOf": [
                  {
                     "additionalProperties": true,
                     "type": "object"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Args passed to the async HTTP client.",
               "title": "Asyncclientargs"
            },
            "extraBody": {
               "anyOf": [
                  {
                     "additionalProperties": true,
                     "type": "object"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Extra parameters to add to the request body.\n      The structure must match the backend API's request structure.\n      - VertexAI backend API docs: https://cloud.google.com/vertex-ai/docs/reference/rest\n      - GeminiAPI backend API docs: https://ai.google.dev/api/rest",
               "title": "Extrabody"
            },
            "retryOptions": {
               "anyOf": [
                  {
                     "$ref": "#/$defs/HttpRetryOptions"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "HTTP retry options for the request."
            }
         },
         "title": "HttpOptions",
         "type": "object"
      },
      "HttpRetryOptions": {
         "additionalProperties": false,
         "description": "HTTP retry options to be used in each of the requests.",
         "properties": {
            "attempts": {
               "anyOf": [
                  {
                     "type": "integer"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Maximum number of attempts, including the original request.\n      If 0 or 1, it means no retries.",
               "title": "Attempts"
            },
            "initialDelay": {
               "anyOf": [
                  {
                     "type": "number"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Initial delay before the first retry, in fractions of a second.",
               "title": "Initialdelay"
            },
            "maxDelay": {
               "anyOf": [
                  {
                     "type": "number"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Maximum delay between retries, in fractions of a second.",
               "title": "Maxdelay"
            },
            "expBase": {
               "anyOf": [
                  {
                     "type": "number"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Multiplier by which the delay increases after each attempt.",
               "title": "Expbase"
            },
            "jitter": {
               "anyOf": [
                  {
                     "type": "number"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "Randomness factor for the delay.",
               "title": "Jitter"
            },
            "httpStatusCodes": {
               "anyOf": [
                  {
                     "items": {
                        "type": "integer"
                     },
                     "type": "array"
                  },
                  {
                     "type": "null"
                  }
               ],
               "default": null,
               "description": "List of HTTP status codes that should trigger a retry.\n      If not specified, a default set of retryable codes may be used.",
               "title": "Httpstatuscodes"
            }
         },
         "title": "HttpRetryOptions",
         "type": "object"
      },
      "ImagePromptLanguage": {
         "description": "Enum that specifies the language of the text in the prompt.",
         "enum": [
            "auto",
            "en",
            "ja",
            "ko",
            "hi",
            "zh",
            "pt",
            "es"
         ],
         "title": "ImagePromptLanguage",
         "type": "string"
      },
      "PersonGeneration": {
         "description": "Enum that controls the generation of people.",
         "enum": [
            "DONT_ALLOW",
            "ALLOW_ADULT",
            "ALLOW_ALL"
         ],
         "title": "PersonGeneration",
         "type": "string"
      },
      "SafetyFilterLevel": {
         "description": "Enum that controls the safety filter level for objectionable content.",
         "enum": [
            "BLOCK_LOW_AND_ABOVE",
            "BLOCK_MEDIUM_AND_ABOVE",
            "BLOCK_ONLY_HIGH",
            "BLOCK_NONE"
         ],
         "title": "SafetyFilterLevel",
         "type": "string"
      }
   },
   "additionalProperties": false
}
Fields:
add_watermark (bool | None)

aspect_ratio (str | None)

enhance_prompt (bool | None)

guidance_scale (float | None)

http_options (genai.types.HttpOptions | None)

image_size (str | None)

include_rai_reason (bool | None)

include_safety_attributes (bool | None)

language (genai.types.ImagePromptLanguage | None)

negative_prompt (str | None)

number_of_images (int | None)

output_compression_quality (int | None)

output_gcs_uri (str | None)

output_mime_type (str | None)

person_generation (genai.types.PersonGeneration | None)

safety_filter_level (genai.types.SafetyFilterLevel | None)

seed (int | None)