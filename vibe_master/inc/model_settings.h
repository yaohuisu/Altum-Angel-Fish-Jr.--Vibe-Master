/*
* Copyright 2019-2020, Synopsys, Inc.
* All rights reserved.
*
* This source code is licensed under the BSD-3-Clause license found in
* the LICENSE file in the root directory of this source tree.
*
*/
#ifndef MODEL_SETTINGS_H_
#define MODEL_SETTINGS_H_

constexpr int kNumCols = 48;
constexpr int kNumRows = 48;
constexpr int kNumChannels = 1;

constexpr int kImageSize = kNumCols * kNumRows * kNumChannels;

constexpr int kCategoryCount = 4;
extern const char* kCategoryLabels[kCategoryCount];
constexpr int kAngryIndex = 0;
constexpr int kHappyIndex = 1;
constexpr int kNormalIndex = 2;
constexpr int kSadIndex = 3;

#endif // MODEL_SETTINGS_H_
