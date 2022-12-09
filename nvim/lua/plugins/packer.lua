local fn = vim.fn
local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
if fn.empty(fn.glob(install_path)) > 0 then
  print ('Installing packer...')
  packer_bootstrap = fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
  print('Done')
end

return require('packer').startup(function(use)

  use 'wbthomason/packer.nvim'
  use 'ackyshake/Spacegray.vim'
  use 'xiyaowong/nvim-transparent'
  -- NEOTREE
  use {
      'nvim-neo-tree/neo-tree.nvim',
      branch = "v2.x",
    requires = {
      "nvim-lua/plenary.nvim",
      "kyazdani42/nvim-web-devicons", -- not strictly required, but recommended
      "MunifTanjim/nui.nvim"
    },
  }
  use 'sidebar-nvim/sidebar.nvim'
 -- FIN NEOTREE
 
 -- LUALINE
  use {
    'nvim-lualine/lualine.nvim',
    requires = { 'kyazdani42/nvim-web-devicons', opt = true }
  }
  -- FIN LUALINE

  -- BUFFERLINE
  -- using packer.nvim
  use {
  'akinsho/bufferline.nvim', 
  tag = "v2.*", 
  requires = 'kyazdani42/nvim-web-devicons'}
  -- FIN BUFFERLINE
 
  -- INDENT-BLANKLINE
  -- init.lua
    use 'lukas-reineke/indent-blankline.nvim'
    -- FIN INDENT-BLANKLINE
    
    --TREE SITTEr
     use {
        'nvim-treesitter/nvim-treesitter',
        run = function() require('nvim-treesitter.install').update({ with_sync = true }) end,
    }
    --FIN TREE SITTER

    use 'wellle/targets.vim'

    -- TELESCOPE    
    use 'nvim-lua/plenary.nvim'
    use {
      'nvim-telescope/telescope.nvim', 
      tag = '0.1.0',-- or                            , branch = '0.1.x',
      requires = { {'nvim-lua/plenary.nvim'} }}
    use 'nvim-telescope/telescope-ui-select.nvim'
    use 'nvim-telescope/telescope-symbols.nvim'
    use 'nvim-telescope/telescope-media-files.nvim'
    use 'nvim-telescope/telescope-file-browser.nvim'

      -- FIN TELESCOPE
      
      -- TOGGLETERMINAL
    use {"akinsho/toggleterm.nvim", tag = '*', config = function() end}
      -- FIN TOGGLETERM

      -- LSPCONFIG
    use 'neovim/nvim-lspconfig' -- Configurations for Nvim LSP
      -- FIN LSPCONFIG

      -- COMMENT
    use {'numToStr/Comment.nvim',
      config = function() end}
      --FIN COMMENT
    
    use 'tpope/vim-fugitive'
    use {
    'lewis6991/gitsigns.nvim',
    requires = { 'nvim-lua/plenary.nvim' },
    config = function()
      require('gitsigns').setup()
    end
  } 
    use 'kdheepak/lazygit.nvim'


    -- CMP AUTOCOMPLETE
      use {
    'hrsh7th/nvim-cmp',
    requires = {
      'L3MON4D3/LuaSnip',
      'hrsh7th/cmp-nvim-lsp',
      'hrsh7th/cmp-path',
      'hrsh7th/cmp-buffer',
      'f3fora/cmp-spell',
      'saadparwaiz1/cmp_luasnip',
      },
    }
    use 'rafamadriz/friendly-snippets'
    use {'onsails/lspkind-nvim'}
    -- FIN AUTOCOMPLETE
    --
--    use {'neoclide/coc.nvim', branch = 'master', run = 'yarn install --frozen-lockfile'}
--
    use "terrortylor/nvim-comment"
    end)
