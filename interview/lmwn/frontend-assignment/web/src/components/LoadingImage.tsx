// @ts-nocheck
import React from "react";
import ContentLoader, { IContentLoaderProps } from "react-content-loader";

export default function LoadingImage(
  props: IContentLoaderProps & React.SVGAttributes<SVGElement>
) {
  return (
    <ContentLoader
      viewBox="0 0 300 300"
      height={"100%"}
      width={"100%"}
      {...props}
    >
      <rect x="0" y="0" rx="5" ry="5" width="100%" height="100%" />
    </ContentLoader>
  );
}
