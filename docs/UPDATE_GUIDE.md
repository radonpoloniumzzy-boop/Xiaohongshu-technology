# 更新与对接

1. 先读当前PROJECT-STATE与用户最新请求；分析、制作、上传、发布分别确认已授权范围。
2. 只在需要时重新核后台；把新快照写入data/snapshots/YYYY-MM-DD，不覆盖旧快照。保留统计起止、采集时间、模块截止、实际发布时间与版本。
3. 用显式字段导出汇总，原网络包/浏览器会话/个人名单留本机；不要直接复制整个账号复盘或工作目录。
4. 更新当前诊断/项目状态；旧结论被取代时在docs/DECISIONS.md说明证据与影响，避免把历史排期重新当指令。
5. 补资产状态时分exists/rendered/sampled/continuous_review/remote_verified等，记录真实范围，不能仅凭技术成功升为已审。
6. 运行python scripts/validate_handoff.py；数据可复算用python scripts/recompute_metrics.py。新增文件后使用--refresh-manifest显式更新文件清单再复查。
7. 提交前检查git diff --stat、敏感内容扫描结果和远程HEAD；只推本次批准内容，保留他人提交。平台发布不由Git提交自动触发。

本库不是运行中服务。无定时任务、自动抓取/投流或自动发文。跨模型交接至少写：目标/约束、已确认与撤回决定、当前证据、未核项、下一步和本次验证。
