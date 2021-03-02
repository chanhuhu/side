import React, { ImgHTMLAttributes } from "react";

const imageCache = new Set<string>();
function prefetchImage(src?: string) {
  if (!src || imageCache.has(src)) {
    return;
  }

  const promise = new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = resolve;
    img.onerror = reject;
    img.src = src;
  }).then(() => {
    imageCache.add(src);
  });

  throw promise;
}

export default function SuspenseImage(
  props: ImgHTMLAttributes<HTMLImageElement>
) {
  prefetchImage(props.src);
  // eslint-disable-next-line
  return <img style={{ display: "block" }} {...props} />;
}
