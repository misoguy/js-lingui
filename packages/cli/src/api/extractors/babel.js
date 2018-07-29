// @flow
import { transformFileSync } from "babel-core"

import linguiExtractMessages from "@lingui/babel-plugin-extract-messages"

import type { ExtractorType } from "./types"

const babelRe = /\.jsx?$/i

const extractor: ExtractorType = {
  match(filename) {
    return babelRe.test(filename)
  },

  extract(filename, localeDir, options = {}) {
    const plugins = options.plugins || []
    transformFileSync(filename, {
      ...options,
      plugins: [[linguiExtractMessages, { localeDir }], ...plugins]
    })
  }
}

export default extractor
