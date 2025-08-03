apply relative paths to concat_vid to allow calls from an outside script and to operate on input/output files for an outside driectory similiar to what was done in main.py in a previous commit:


commit 975d6b9d89f14b9653690d209e8fdafa921d180a
Author: sutt <wsutton17@gmail.com>
Date:   Wed Jul 30 19:18:58 2025 -0400

    fix: expand scripting relative paths to all inputs

diff --git a/main.py b/main.py
index 5b5e910..a574af6 100644
--- a/main.py
+++ b/main.py
@@ -411,6 +411,27 @@ def main():
 
     args = parser.parse_args()
 
+    # Resolve relative paths against caller's directory
+    if "VIDSTR_CALLER_DIR" in os.environ:
+        caller_dir = os.environ["VIDSTR_CALLER_DIR"]
+        
+        # Resolve output directory
+        if hasattr(args, "output_dir") and args.output_dir and not os.path.isabs(args.output_dir):
+            args.output_dir = os.path.join(caller_dir, args.output_dir)
+        
+        # Resolve input paths
+        if hasattr(args, "input_image") and args.input_image and not os.path.isabs(args.input_image):
+            args.input_image = os.path.join(caller_dir, args.input_image)
+        
+        if hasattr(args, "input_video") and args.input_video and not os.path.isabs(args.input_video):
+            args.input_video = os.path.join(caller_dir, args.input_video)
+        
+        if hasattr(args, "last_frame") and args.last_frame and not os.path.isabs(args.last_frame):
+            args.last_frame = os.path.join(caller_dir, args.last_frame)
+        
+        if hasattr(args, "video") and args.video and not os.path.isabs(args.video):
+            args.video = os.path.join(caller_dir, args.video)
+
     if args.vertex:
         os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"
     else:
