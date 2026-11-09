# 接班入口

## 先读的当前结论

1. 账号有自然推荐和新增关注。周对周观看3613→5229、新增41→70；但周内放量后回落。11/6点击17.2%高于11/1的15.7%、均看更长，曝光却12406→2191，不能统一归罪封面片头。
2. 增长集中：糖盒累计观看约77.5%；不是本周/月贡献。新稿受限/未成熟与内容差分开。
3. 观看来源7日首页69/视频13/搜索13/其他5%；粉丝来源显示74.49/21.43/1.02/3.06，窗口未明，不能相除算渠道转化。
4. 女性粉丝39%；糖盒、套娃、机器鸭、烤箱、扫地机都有女性观众过半样本。观众占比不是新增女性粉丝，缺性别分段关注。
5. 账号周均看14.7秒、环比−17%；点赞每千观看31.55低于40.96；收藏接近月均，评论3对4样本很小。全号关注事件密度上升，不等于所有路径都好：月主页转粉1.8%、相对−41%，周3.3%，尚需呈现证据。

## 按任务取文件

- 继续账号诊断：reports/current-account-diagnosis.md → data/snapshots/2026-11-08/account.json、daily-30.json、notes-41.json。
- 逐篇内容：reports/notes-23-analysis.md → review-evidence-23.json、retention-curves.json、timing-23.json。需要重看片须先取得资产，不能只读结论声称看完。
- 查成片/草稿：docs/PIPELINE.md → data/batches/seven-bgm-20261103.json 与 data/projects/inventory.json。
- 查新五题：data/batches/five-topics-20261108.json。18条视频仅7条实拍或混合，11条CG辅助，仍有缺口。
- 做跨机接续：docs/LOCAL_ASSETS.md、docs/UPDATE_GUIDE.md。

## 不要继承的旧决定

旧“五槽发布日历”、某时段最佳、所有视频压成30秒、可爱或实用题已胜出、所有片头/封面差，都不是当前已确认事实。历史增长策略只作为候选，当前不排产。

## 最小验证

运行 python scripts/validate_handoff.py；用 python scripts/recompute_metrics.py 复算计数密度与推荐来源。执行新工作前检查用户本轮授权、数据日期、版本、媒体可用性和已有草稿，避免重复上传。
