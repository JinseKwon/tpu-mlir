//===----------------------------------------------------------------------===//
//
// Copyright (C) 2022 Sophgo Technologies Inc.  All rights reserved.
//
// TPU-MLIR is licensed under the 2-Clause BSD License except for the
// third-party components.
//
//===----------------------------------------------------------------------===//

#pragma once

#include "oneapi/dnnl/dnnl.hpp"

using namespace dnnl;
namespace tpu_mlir {

typedef struct {
  int64_t n;
  int64_t c;
  int64_t id;
  int64_t ih;
  int64_t iw;
  int64_t od;
  int64_t oh;
  int64_t ow;
  int64_t kd;
  int64_t kh;
  int64_t kw;
  int64_t sd;
  int64_t sh;
  int64_t sw;
  int64_t pad_d;
  int64_t pad_d_after;
  int64_t pad_h;
  int64_t pad_h_after;
  int64_t pad_w;
  int64_t pad_w_after;
  int64_t pad_value;
  bool    do_relu;
  double  relu_limit;
  bool    is_global;
  bool    count_include_pad;
} pool_attr_t;

class Pooling {
public:
  Pooling();
  ~Pooling();
  void setup(float *input, float *output, pool_attr_t attr, bool is_avg,
             int izp = 0);
  void run();
private:
  void pad_init(float *input, pool_attr_t &attr, int izp);
public:
  int kd, kh, kw;

private:
  engine eng;
  stream eng_stream;
  std::vector<primitive> net;
  std::vector<std::unordered_map<int, memory>> net_args;
  pooling_forward::primitive_desc prim_desc;
  memory::dims src_shape;
  memory::dims dst_shape;
  float *p_input;
  float *origin_input;
  std::shared_ptr<std::vector<float>> input_after_pad;
  pool_attr_t _attrs;
  int _izp;
};
} // namespace tpu_mlir
