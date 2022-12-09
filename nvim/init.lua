--[[
  ██╗███╗   ██╗██╗████████╗██╗     ██╗   ██╗ █████╗
  ██║████╗  ██║██║╚══██╔══╝██║     ██║   ██║██╔══██╗
  ██║██╔██╗ ██║██║   ██║   ██║     ██║   ██║███████║
  ██║██║╚██╗██║██║   ██║   ██║     ██║   ██║██╔══██║
  ██║██║ ╚████║██║   ██║██╗███████╗╚██████╔╝██║  ██║
  ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
Neovim init file
Version: 0.8.0
Maintainer: Brainf+ck
Website: https://github.com/brainfucksec/neovim-lua
--]]


-- ARCHIVOS DE CONFIG / PLUGINS
require	('settings')
require	('keymaps')
require ('plugins/packer')
require	('plugins/neo-tree')           -- filebrowser
require ('plugins/lualine')
require ('plugins/bufferline')
require ('plugins/indent-blankline')
require ('plugins/treesitter')
require ('plugins/telescope')
require ('plugins/telescope-ui')
require ('plugins/telescope-media')
require ('plugins/toggleterm')
require ('plugins/gitsigns')
require ('plugins/lsp-config')
require ('plugins/cmp')
--require ('plugins/coc')
require ('plugins/nvim-comment')
vim.api.nvim_set_option("clipboard","unnamed")
vim.g.transparent_enabled=true
