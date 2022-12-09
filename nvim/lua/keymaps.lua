-- Aliases

local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}
local cmd = vim.cmd

--Desactiva los teclas direccionales
--map('', '<up>', '<nop>', {noremap = true})
--map('', '<down>', '<nop>', {noremap = true})
--map('', '<left>', '<nop>', {noremap = true})
--map('', '<right>', '<nop>', {noremap = true})

map('n', '<C-n>', ':Neotree toggle<CR>', default_opts)       -- open/:wqclose
