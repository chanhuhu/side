import React, { LiHTMLAttributes } from "react";
import "./Tag.css";

type Props = {
  tagName: string;
} & LiHTMLAttributes<HTMLLIElement>;

export default function Tag({ tagName, ...props }: Props) {
  return (
    <li className="tag" {...props}>
      {tagName}
    </li>
  );
}
