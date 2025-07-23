# Dev Summary
Looks at tasks and associated commit solutions generated each release.

## v0.0.1

| Task File | Description | Commit |
|-----------|-------------|--------|
| [test-script.md](.public-agdocs/specs/test-script.md) | Build a simple test script that calls main functionality with visual separation for each command | [5b82da1](https://github.com/sutt/vidstr/commit/5b82da1) |
| [finalize-vidcont.md](.public-agdocs/specs/finalize-vidcont.md) | Remove debugging conditions from vertex video continuation and add explicit bucket filepath prefix | [7cf8d94](https://github.com/sutt/vidstr/commit/7cf8d94) |
| [v4-fixcont.md](.public-agdocs/specs/v4-fixcont.md) | Fix video generation logic with bucket output for --vertex option, utilize gs://hello-world-123 bucket | [74fc970](https://github.com/sutt/vidstr/commit/74fc970) |
| [need-bucket.md](.public-agdocs/specs/need-bucket.md) | n/a | n/a |
| [client-type.md](.public-agdocs/specs/client-type.md) | Add proper type hint to client argument in main | [6aefc68](https://github.com/sutt/vidstr/commit/6aefc68) |
| [v3-fix-vidcont.md](.public-agdocs/specs/v3-fix-vidcont.md) | Fix AttributeError when response is NoneType in video generation | [3a24cd9](https://github.com/sutt/vidstr/commit/3a24cd9) |
| [v2-fix-vidcont.md](.public-agdocs/specs/v2-fix-vidcont.md) | n/a | n/a |
| [fix-vidcont.md](.public-agdocs/specs/fix-vidcont.md) | n/a | n/a |
| [vertex-to-main.md](.public-agdocs/specs/vertex-to-main.md) | Add CLI option for vertex, keep client.py but bring vertex auth switch to main.py | [3470693](https://github.com/sutt/vidstr/commit/3470693) |
| [gen-start-vid.md](.public-agdocs/specs/gen-start-vid.md) | Add optional argument to generate video with starting video using video extension | [572145e](https://github.com/sutt/vidstr/commit/572145e) |
| [unique-fn.md](.public-agdocs/specs/unique-fn.md) | Add unique filename behavior with incremental counter for image gen, video gen, and get_frame | [ea8c760](https://github.com/sutt/vidstr/commit/ea8c760) |
| [cont-func.md](.public-agdocs/specs/cont-func.md) | Create continue_video function that uses get_frame --frame 'last' and creates video from last frame | [572145e](https://github.com/sutt/vidstr/commit/572145e) |
| [img-to-vid.md](.public-agdocs/specs/img-to-vid.md) | Create video function with starting image argument, add logic to switch between image and video creation | [10abf42](https://github.com/sutt/vidstr/commit/10abf42) |
| [fix-imwrite.md](.public-agdocs/specs/fix-imwrite.md) | Fix cv2.imwrite error when output path lacks proper file extension | [6ab75ae](https://github.com/sutt/vidstr/commit/6ab75ae) |
| [get-frame.md](.public-agdocs/specs/get-frame.md) | Write CLI utility to grab first or last frame of video mp4 downloaded to data/tmp | [2b68fec](https://github.com/sutt/vidstr/commit/2b68fec) |
| [make-img.md](.public-agdocs/specs/make-img.md) | Create generate_images function with CLI for calling with prompt and optional params, download to data/tmp | [fae336d](https://github.com/sutt/vidstr/commit/fae336d) |
| [setup-vertex.md](.public-agdocs/specs/setup-vertex.md) | Create option to connect to Vertex AI with client, add env vars and test connection function | [7ab2bcc](https://github.com/sutt/vidstr/commit/7ab2bcc) |
