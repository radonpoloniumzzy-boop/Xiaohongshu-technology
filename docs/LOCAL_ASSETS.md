# 离线资产与跨机接续

此库不含视频、音频、封面图、剪映草稿或原始网络包。报告中原本指向本机证据的链接统一指向本页，不能因此声称云端已经重看。

逻辑根：VIDEO_PROJECTS_ROOT（每期作品）、RESEARCH_ROOT（选题研究）、ANALYTICS_ROOT（本次完整分析）、MEDIA_ROOT（原片来源包）。在本机config/local-roots.local.json填实际路径，该文件被Git忽略；跨机由资料所有者提供授权副本并重新绑定。

- [已发布分析副本索引](../assets/media-index.json)：23个asset_id、逻辑路径、片长、字节和已有SHA。
- [作品目录](../data/projects/inventory.json)：56个目录的状态来源及本地成片文件；sha256为null表示本次只盘点存在性，未读媒体计算哈希。
- [七篇BGM批次](../data/batches/seven-bgm-20261103.json)：增强版候选、4封面逻辑位置与文件存在性，远程草稿完整性待核。
- [新五题缺口](../data/batches/five-topics-20261108.json)：只给素材覆盖，不把CG当实拍或文件数当可剪程度。

取得素材后复核hash/长度/版本，实际审看片段再记录。平台转码后字节可能变化，本地与发布版不能仅凭文件名或mtime判同一；身份与内容范围分别验证。原始来源与商业使用许可分开，公开本库不授予第三方媒体重用许可。
