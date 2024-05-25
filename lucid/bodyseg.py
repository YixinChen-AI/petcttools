import argparse
from lucid_utils_low import lucid

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LUCIDA : body segmentation")
    parser.add_argument("--ct", type=str, help="the nii.gz path for ct.nii.gz")
    parser.add_argument("--output", type=str, help="the output direction path for segmentation output")
    args = parser.parse_args()

    print(f"CT Path: {args.ct}")
    print(f"Output Path: {args.output}")

    lucid(args.ct,
          output_seg_path=args.output,
          output_stdct_path=None,
          check=True,
          modelname="STUNet_large",
          modelweight="./STUNet_large.pth",
          output=None)
